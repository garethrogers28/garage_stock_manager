"""
Garage Stock Manager -
A command-line application to manage vehicle inventory for a used car garage.
"""

import gspread
from google.oauth2.service_account import Credentials
from datetime import date
from tabulate import tabulate
import re
import os


# 1. SETUP / API CONNECTION


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("garage_stock_manager")


# 2. HELPER FUNCTIONS
#    - Generic reusable functions


def safe_sheet_call(func, *args, **kwargs):
    """
    Safely call a Google Sheets API function.
    Return None if there is an error.
    """
    try:
        # Attempt the API call
        return func(*args, **kwargs)
    except Exception as e:
        print(f"\nError accessing Google Sheet: {e}")
        return None


def get_stock_sheet():
    """
    Return the stock worksheet from the Google Sheet.
    """
    # Directly access the 'stock' worksheet
    return SHEET.worksheet("stock")


def get_stock(sheet):
    """
    Return stock records or None if empty or on error.
    Normalize all vehicle IDs to integers.
    """
    # Safe_sheet_call to handle potential API errors
    stock = safe_sheet_call(sheet.get_all_records)
    if stock is None:  # API error
        return None

    if not stock:
        print("\nNo vehicles in stock.")
        return None
    # Convert all 'id' fields to integers for consistency
    for vehicle in stock:
        try:
            vehicle["id"] = int(vehicle["id"])
        except (ValueError, TypeError):
            print("\nInvalid vehicle ID found in stock data.")
            return None

    return stock


def require_stock_or_exit():
    """
    Retrieve the stock sheet and stock data.
    Exit early with a user-friendly message if unavailable.
    """
    # Get the sheet
    sheet = safe_sheet_call(SHEET.worksheet, "stock")
    if sheet is None:
        print(
            "\nUnable to access the stock worksheet. "
            "Check your internet/API connection."
        )
        return None, None

    # Get the current stock
    stock = get_stock(sheet)

    if stock is None:
        print(
            "\nUnable to retrieve stock data "
            "Please check your internet/API connection and try again."
        )
        return None, None

    if not stock:
        stock = []

    return sheet, stock


def find_vehicle_by_id(stock, vehicle_id):
    """
    Return the vehicle dict and its row number in the sheet,
    or (None, None) if not found.
    """
    for index, vehicle in enumerate(
        stock, start=2
    ):  # start=2 to account for header row being 1
        try:
            if (vehicle["id"]) == vehicle_id:
                return vehicle, index
        except ValueError:
            continue
    return None, None

def clear_screen():
    """
    Clear the terminal screen.
    Works on Windows, macOS, and Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# 3. USER INPUT FUNCTIONS
#    - Functions that validate and sanitize input


def get_required_input(prompt):
    """Prevent empty entry function"""
    while True:
        value = input(prompt).strip()  # Strip() to remove leading/trailing spaces
        if value:
            return value
        else:
            print("This field cannot be empty. Please enter a value.")


def get_valid_year(prompt, min_year=2001, max_year=2028):
    """
    Prompt the user to enter a year and validate
    it falls within min_year and max_year.

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
                print(f"\nPlease enter a valid year between {min_year} and {max_year}.")
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


def validate_registration(reg):
    """
    Validate UK vehicle registration (2001 onwards format).
    Format: AA21 ABC
    """
    pattern = r"^[A-Z]{2}[0-9]{2}\s?[A-Z]{3}$"
    return re.match(pattern, reg.upper()) is not None


def get_valid_registration(stock):
    """
    Prompt the user for a UK registration number.
    Validate format and check it's not already in stock.
    """
    while True:
        reg = (
            input("\nEnter vehicle registration number (e.g., CN18 YGG): ")
            .upper()
            .strip()
        )
        if not validate_registration(reg):
            print("\nInvalid registration format. Please use the format AA12 ABC.")
            continue
        # Check if registration already exists
        if stock and any(v["reg_number"].upper() == reg for v in stock):
            print(
                "\nThis registration already exists in stock. Please enter a different one."
            )
            continue
        return reg


# 4. DISPLAY FUNCTIONS
#    - Functions that show information to the user


def get_user_choice():
    """
    Get the user choice and
    Validate the input to ensure it's between 1 and 4.
    """
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice in ["1", "2", "3", "4"]:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def display_main_menu():
    """
    Display the main menu to the user.
    Show 4 options:
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


def view_all_vehicles():
    """
    Display all vehicles in stock.
    Fits neatly in Heroku terminal.
    Purchase price column removed to save width.
    """
    sheet, stock = require_stock_or_exit()
    if not stock:
        return

    print("\nCurrent Vehicles in Stock:\n")

    # Prepare table data
    table_data = [
        [
            vehicle["id"],
            vehicle["reg_number"],
            vehicle["make"],
            vehicle["model"],
            vehicle["year"],
            vehicle["mileage"],
            vehicle["sale_price"],
            vehicle["status"],
        ]
        for vehicle in stock
    ]

    headers = ["ID", "Reg", "Make", "Model", "Year", "Mileage", "Price", "Status"]

    # Max widths per column (mostly for very long text)
    max_widths = [4, 10, 10, 10, 4, 7, 8, 10]

    # Truncate only very long text (numbers stay as-is)
    table_data = [
        [
            str(cell) if isinstance(cell, (int, float))
            else (cell if len(cell) <= w else cell[:w-3] + "...")
            for cell, w in zip(row, max_widths)
        ]
        for row in table_data
    ]

    # Print table
    print(tabulate(table_data, headers=headers, tablefmt="simple"))


# 5. VEHICLE MANAGEMENT FUNCTIONS
#    - Add, remove vehicles


def add_vehicle():
    """
    Add a new vehicle to the garage stock sheet and validate user input.
    """
    sheet, stock = require_stock_or_exit()

    # Determine next ID automatically based on existing stock,
    # ensuring we handle the case where stock is empty by defaulting to 1.
    next_id = max([v["id"] for v in stock], default=0) + 1

    reg_number = get_valid_registration(stock)

    make = get_required_input("\nEnter vehicle make (e.g., Ford): ").title()
    model = get_required_input("\nEnter vehicle model  (e.g., Fiesta): ").title()
    year = get_valid_year("\nEnter vehicle year (e.g., 2018): ")
    mileage = get_valid_int("\nEnter vehicle mileage  (e.g., 50000): ")
    purchase_price = get_valid_float("\nEnter vehicle purchase price (e.g., 8000): ")
    sale_price = get_valid_float("\nEnter vehicle sale price  (e.g., 10000): ")

    status = "For Sale"
    date_added = date.today().strftime("%Y-%m-%d")

    # Append the new vehicle to the Google Sheet
    success = safe_sheet_call(
        sheet.append_row,
        [
            next_id,
            reg_number,
            make,
            model,
            year,
            mileage,
            purchase_price,
            sale_price,
            status,
            date_added,
        ],
    )

    if success is not None:
        print(f"\nVehicle ID {next_id} ({reg_number}) added successfully!")
    else:
        print("\nFailed to add vehicle due to API error.")


def remove_vehicle():
    """
    Remove a vehicle from the garage stock sheet based on vehicle ID,
    with a confirmation prompt before deletion.
    User can press Enter to return to the main menu.
    """
    sheet, stock = require_stock_or_exit()
    if not stock:
        return

    # Show all vehicles so user can choose
    view_all_vehicles()

    while True:
        user_input = input("\nEnter vehicle ID to remove or press Enter to return to main menu: ").strip()
        if user_input == "":
            print("\nReturning to main menu...")
            return  # Exit function without removing

        # Validate numeric input using your helper
        try:
            vehicle_id = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid numeric ID or press Enter to go back.")
            continue

        vehicle, row_number = find_vehicle_by_id(stock, vehicle_id)

        if vehicle:
            confirm = input(
                f"\nAre you sure you want to remove Vehicle ID {vehicle_id} "
                f"({vehicle['reg_number']})? (y/n): "
            ).strip().lower()

            if confirm == "y":
                success = safe_sheet_call(sheet.delete_rows, row_number)
                if success is not None:
                    print(
                        f"\nVehicle ID {vehicle_id} ({vehicle['reg_number']}) removed successfully!"
                    )
                else:
                    print("\nFailed to remove vehicle due to API error.")
            else:
                print("\nRemoval cancelled.")
            break
        else:
            print(f"\nVehicle ID {vehicle_id} not found. Please review the list and try again.")


def main():
    """
    Main program loop for Garage Stock Manager.
    Displays the main menu and handles user choices until exit.
    """
    while True:
        display_main_menu()
        choice = get_user_choice()

        if choice == 1:
            view_all_vehicles()
            input("\nPress Enter to return to the main menu...\n")
            clear_screen()
        elif choice == 2:
            add_vehicle()
        elif choice == 3:
            remove_vehicle()
        elif choice == 4:
            print("\nExiting Garage Stock Manager. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
