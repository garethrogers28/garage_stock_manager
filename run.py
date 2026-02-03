import gspread
from google.oauth2.service_account import Credentials
from datetime import date

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('garage_stock_manager')

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
    print("1. View all vehicles")
    print("2. Add a vehicle")
    print("3. Remove a vehicle")
    print("4. Exit")

def get_user_choice():
    """
    Get the user's choice and
    Validates the input to ensure it's between 1 and 4.
    """
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def view_all_vehicles():
    """
    Displays all vehicles in the garage stock.
    """

    sheet = SHEET.worksheet('stock')
    stock = sheet.get_all_records()
    
    #Checks to see if the sheet is empty, prints error message if it is. 
    
    if not stock:
        print("\nNo vehicles in stock.")
    else:
        print("\nCurrent Vehicles in Stock:")
        for vehicle in stock:
            print(f"ID: {vehicle['id']}, Make: {vehicle['make']}, Model: {vehicle['model']}, Year: {vehicle['year']}, Mileage: {vehicle['mileage']}, Sale Price: {vehicle['sale_price']}, Status: {vehicle['status']}")


# Validating year
def get_valid_year(prompt, min_year=1975, max_year=2028):
    while True:
        try:
            year = int(input(prompt))
            if min_year <= year <= max_year:
                return year
            else:
                print(f"Please enter a valid year between {min_year} and {max_year}.")
        except ValueError:
            print("Invalid input. Please enter a numeric year.")

# Validate Integer for mileage function
def get_valid_int(prompt, min_value=0):
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Please enter a number greater than or equal to {min_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Validate Float for sale/purchase price function
def get_valid_float(prompt, min_value=0):
    while True:
        try:
            price = float(input(prompt))
            if price >= min_value:
                return price
            else:
                print(f"Value must be at least {min_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")



def add_vehicle():
    """
    Adds a new vehicle to the garage stock sheet.
    """
    sheet = SHEET.worksheet('stock')

     # Get existing stock to calculate next ID
    stock = sheet.get_all_records()
    if stock:
        next_id = max(vehicle['id'] for vehicle in stock) + 1
    else:
        next_id = 1

    # asks user for vehicle details
    reg_number = input("Enter vehicle registration number (e.g., CN18 YGG): ").upper()
    make = input("Enter vehicle make (e.g., Ford): ").title()
    model = input("Enter vehicle model (e.g., Fiesta): ").title()
    year = get_valid_year("Enter vehicle year (e.g., 2018): ")
    mileage = get_valid_int("Enter vehicle mileage (e.g., 50000): ")
    purchase_price = get_valid_float("Enter vehicle purchase price (e.g., 8000): ")
    sale_price = get_valid_float("Enter vehicle sale price (e.g., 10000): ")

    # Default status is 'For Sale' and auto date/time
    status = 'For Sale' 
    date_added = date.today().strftime("%Y-%m-%d")

    # Append new vehicle to the sheet
    sheet.append_row([next_id, reg_number, make, model, year, mileage, purchase_price, sale_price, status, date_added])

    print(f"\nVehicle ID {next_id} ({reg_number}) added successfully!")


    
              
def main():
    """
    Main program loop.
    """
    while True:
        display_main_menu()
        choice = get_user_choice()
        
        if choice == 1:
            view_all_vehicles()
            input("\nPress Enter to return to the main menu...")

        elif choice == 2:
            add_vehicle()

        elif choice == 3:
            print("\nRemove vehicle feature coming soon...")

        elif choice == 4:
            print("Exiting Garage Stock Manager. Goodbye!")
            break
        
if __name__ == "__main__":
    main()



