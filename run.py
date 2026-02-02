import gspread
from google.oauth2.service_account import Credentials

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
    """
    Checks to see if the sheet is empty, prints error message if it is. 
    """
    if not stock:
        print("\nNo vehicles in stock.")
    else:
        print("\nCurrent Vehicles in Stock:")
        for vehicle in stock:
            print(f"ID: {vehicle['id']}, Make: {vehicle['make']}, Model: {vehicle['model']}, Year: {vehicle['year']}, Mileage: {vehicle['mileage']}, Sale Price: {vehicle['sale_price']}, Status: {vehicle['status']}")

def add_vehicle():
    """
    Adds a new vehicle to the garage stock sheet.
    Validates input and appends the vehicle as a new row.
    """
    sheet = SHEET.worksheet('stock')

    # asks user for vehicle details
    reg_number = input("Enter vehicle registration number (e.g., CN18 YGG): ").upper()
    make = input("Enter vehicle make (e.g., Ford): ").title()
    model = input("Enter vehicle model (e.g., Fiesta): ").title()

    # Validate numeric input year
    while True:
        try:
            year = int(input("Enter vehicle year (e.g., 2018): "))
            if 1975 <= year <= 2028:
                break
            else:
                print("Please enter a valid year between 1975 and 2028.")
        except ValueError:
            print("Invalid input. Please enter a numeric year.")

    # Validate numeric input for mileage
    while True:
        try:
            mileage = int(input("Enter vehicle mileage (e.g., 50000): "))
            if mileage >= 0:
                break
            else:
                print("Mileage cannot be negative. Please enter a valid mileage.")
        except ValueError:
            print("Invalid input. Please enter a number for the mileage.")
      
                 
 



     


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
            print("Add vehicle feature coming soon...")
        elif choice == 3:
            print("Remove vehicle feature coming soon...")
        elif choice == 4:
            print("Exiting Garage Stock Manager. Goodbye!")
            break
if __name__ == "__main__":
    main()



