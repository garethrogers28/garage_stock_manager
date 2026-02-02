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

display_main_menu()

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
get_user_choice()            