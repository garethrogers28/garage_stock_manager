"""
Garage Stock Manager - A command-line application to manage vehicle inventory for a used car garage.
"""

import gspread
from google.oauth2.service_account import Credentials
from datetime import date

# =========================================
# 1. SETUP / API CONNECTION
# =========================================

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('garage_stock_manager')

# =========================================
# 2. HELPER FUNCTIONS
#    - Generic reusable functions
# =========================================

def safe_sheet_call(func, *args, **kwargs):
    """
    Safely call a Google Sheets API function.
    Returns None if there is an error.
    """
    try:
        # Attempt the API call
        return func(*args, **kwargs)
    except Exception as e:
        print(f"\nError accessing Google Sheet: {e}")
        return None

def get_stock_sheet():
    """
    Returns the stock worksheet from the Google Sheet.
    """
     # Directly access the 'stock' worksheet, assuming it exists and is correctly named.
    return SHEET.worksheet('stock')


def get_stock(sheet):
    """
    Returns stock records or None if empty or on error.
    Normalizes all vehicle IDs to integers.
    """
    # safe_sheet_call to handle potential API errors
    stock = safe_sheet_call(sheet.get_all_records)
    if stock is None:  # API error
        return None

    if not stock: # Sheet is empty
        print("\nNo vehicles in stock.")
        return None
    
     # Convert all 'id' fields to integers for consistency
    for vehicle in stock:
        try:
            vehicle['id'] = int(vehicle['id'])
        except (ValueError, TypeError):
            print("\nInvalid vehicle ID found in stock data.")
            return None

    return stock

def require_stock_or_exit():
    """
    Retrieves the stock sheet and stock data.
    Exits early with a user-friendly message if unavailable.
    """
    # Get the sheet
    sheet = get_stock_sheet()
    # Get the current stock
    stock = get_stock(sheet)

    if stock is None: # Could not retrieve stock data (either empty or API error)
        print("\nUnable to retrieve stock data. Please check your internet/API connection and try again.")
        return None, None
    
    return sheet, stock

    
def find_vehicle_by_id(stock, vehicle_id):
    """
    Returns the vehicle dict and its row number in the sheet, or (None, None) if not found.
    """
    for index, vehicle in enumerate(stock, start=2): # start=2 to account for header row being 1
        try:  
            if (vehicle['id']) == vehicle_id:
                return vehicle, index
        except ValueError:
            continue
    return None, None

# =========================================
# 3. USER INPUT FUNCTIONS
#    - Functions that validate and sanitize input
# =========================================


def get_required_input(prompt):
    """Prevent empty entry function"""
    while True:
        
        value = input(prompt).strip()# strip() to remove leading/trailing spaces, ensuring we don't accept input that is just spaces
        if value:
            return value
        else:
            print("This field cannot be empty. Please enter a value.")


def get_valid_year(prompt, min_year=1975, max_year=2028):
    """
    Prompt the user to enter a year and validate it falls within min_year and max_year.

    Args:
        prompt (str): The message shown to the user.
        min_year (int): Minimum allowable year.
        max_year (int): Maximum allowable year.

    Returns:
        int: A valid year within the specified range.
    """
    while True:
        try:
            year = int(input(prompt))
            if min_year <= year <= max_year:
                return year
            else:
                print(f"Please enter a valid year between {min_year} and {max_year}.")
        except ValueError:
            print("Invalid input. Please enter a numeric year.")


def get_valid_int(prompt, min_value=0):
    """Prompt the user for an integer >= min_value."""
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Please enter a number greater than or equal to {min_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            

def get_valid_float(prompt, min_value=0):
    """Prompt the user for a float >= min_value."""
    while True:
        try:
            price = float(input(prompt))
            if price >= min_value:
                return price
            else:
                print(f"Value must be at least {min_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

            

# =========================================
# 4. DISPLAY FUNCTIONS
#    - Functions that show information to the user
# =========================================


def get_user_choice():
    """
    Get the user's choice and
    Validates the input to ensure it's between 1 and 4.
    """
    while True:
        choice = input("Enter your choice (1-4): ") # No need to strip() here since we're checking for specific valid inputs, and any leading/trailing spaces would make it invalid anyway.
        if choice in ['1', '2', '3', '4']:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def display_main_menu():
    """
    Display the main menu to the user.
    Shows the 4 options:
    1. View all vehicles
    2. Add a vehicle
    3. Remove a vehicle
    4. Exit
    """
    print("\nWelcome to Garage Stock Manager\n")
    print("Please choose an option:")
    print("\n1. View all vehicles")
    print("2. Add a vehicle")
    print("3. Remove a vehicle")
    print("4. Exit\n")

def view_all_vehicles(stock=None):# Allow passing stock data to avoid redundant API calls if we already have it, improving efficiency when called from other functions like remove_vehicle.
    """
    Display all vehicles in stock.

    Args:
        stock (list[dict], optional): List of vehicle records. 
                                      If None, fetches from Google Sheet.
    Returns:
        None
    """
    if stock is None:
        sheet = get_stock_sheet()
        stock = get_stock(sheet)
        if not stock:
            return
    
    print("\nCurrent Vehicles in Stock:\n")
    for vehicle in stock:
        print(
        f"ID: {vehicle['id']}, "
        f"Registration: {vehicle['reg_number']}, "
        f"Make: {vehicle['make']}, "
        f"Model: {vehicle['model']}, "
        f"Year: {vehicle['year']}, "
        f"Mileage: {vehicle['mileage']}, "
        f"Sale Price: {vehicle['sale_price']}, "
        f"Status: {vehicle['status']}\n"
    )

# =========================================
# 5. VEHICLE MANAGEMENT FUNCTIONS
#    - Add, remove vehicles
# =========================================

def add_vehicle():
    """
    Adds a new vehicle to the garage stock sheet with validated user input.
    """
    # Ensure we have stock before proceeding, and get the sheet and current stock data for ID generation and appending.
    sheet, stock = require_stock_or_exit()
    if not stock:
        return
    
    # Determine next ID automatically based on existing stock, ensuring we handle the case where stock is empty by defaulting to 1.
    next_id = max([v['id'] for v in stock], default=0) + 1

    # Collect vehicle data from user with validation to ensure all required fields are filled and correctly formatted.
    reg_number = get_required_input("\nEnter vehicle registration number (e.g., CN18 YGG): ").upper()
    make = get_required_input("\nEnter vehicle make (e.g., Ford): ").title()
    model = get_required_input("\nEnter vehicle model (e.g., Fiesta): ").title()
    year = get_valid_year("\nEnter vehicle year (e.g., 2018): ")
    mileage = get_valid_int("\nEnter vehicle mileage (e.g., 50000): ")
    purchase_price = get_valid_float("\nEnter vehicle purchase price (e.g., 8000): ")
    sale_price = get_valid_float("\nEnter vehicle sale price (e.g., 10000): ")

    
    status = 'For Sale'
    date_added = date.today().strftime("%Y-%m-%d")

    # Append the new vehicle to the Google Sheet, handling potential API errors gracefully
    success = safe_sheet_call(
        sheet.append_row,
        [next_id, reg_number, make, model, year, mileage, purchase_price, sale_price, status, date_added]
    )

    if success is not None:
        print(f"\nVehicle ID {next_id} ({reg_number}) added successfully!")
    else:
        print("\nFailed to add vehicle due to API error.")


def remove_vehicle():
    """
    Removes a vehicle from the garage stock sheet based on vehicle ID,
    with a confirmation prompt before deletion.
    """
    sheet, stock = require_stock_or_exit()
    if not stock:
        return
    
    # Show all vehicles so user can choose
    view_all_vehicles(stock)

    while True:
        # Ask which vehicle to remove by ID, validating input and confirming existence before attempting deletion
        vehicle_id = get_valid_int("\nEnter vehicle ID to remove: ", min_value=1)
        vehicle, row_number = find_vehicle_by_id(stock, vehicle_id)

        if vehicle:
            # Confirm deletion with the user, showing the vehicle's registration number for clarity
            confirm = input(f"Are you sure you want to remove Vehicle ID {vehicle_id} ({vehicle['reg_number']})? (y/n): ").strip().lower()# strip() to remove leading/trailing spaces, lower() to standardize input

            if confirm == 'y':
                success = safe_sheet_call(sheet.delete_rows, row_number)
                if success is not None:
                    print(f"\nVehicle ID {vehicle_id} ({vehicle['reg_number']}) removed successfully!")
                else:
                    print("\nFailed to remove vehicle due to API error.")  
                
            else:
                print("\nRemoval cancelled.")
            break
        else:
            print(f"\nVehicle ID {vehicle_id} not found, please review the list and try again.")

        
def main():
    """
    Main program loop for Garage Stock Manager. Displays the main menu and handles user choices until exit.
    """
    while True:
        display_main_menu()
        choice = get_user_choice()
        
        if choice == 1:
            view_all_vehicles()
            input("\nPress Enter to return to the main menu...\n")

        elif choice == 2:
            add_vehicle()

        elif choice == 3:
            remove_vehicle()                                                        
            
        elif choice == 4:
            print("\nExiting Garage Stock Manager. Goodbye!\n")
            break
        
if __name__ == "__main__":
    main()
   
