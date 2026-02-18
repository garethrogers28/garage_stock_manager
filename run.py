"""
Garage Stock Manager

A command-line application to manage vehicle
inventory for a used car garage.

Features:
- View all vehicles in stock
- Add a new vehicle with validation
- Remove vehicles with confirmation
- Stores data in a Google Sheet
"""

import gspread
from google.oauth2.service_account import Credentials
from datetime import date
from tabulate import tabulate
import re
import os


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("garage_stock_manager")


def safe_sheet_call(func, *args, **kwargs):
    """
    Safely call a Google Sheets API function.

    Args:
        func (callable): The gspread function to call.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        Any: The result of the function call,
        or None if an error occurred.
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
    Retrieve all vehicle records from the stock worksheet.

    Args:
        sheet (gspread.models.Worksheet): The Google Sheet worksheet object.

    Returns:
        list[dict]: List of vehicle records with 'id'
        converted to integers.
        []: If no vehicles are in stock.
        None: If an API error occurs or a vehicle ID is invalid.
    """
    # Attempt to fetch all records from the sheet
    stock = safe_sheet_call(sheet.get_all_records)
    if stock is None:  # API error
        return None

    if not stock:  # No vehicles in stock
        return []

    # Convert all 'id' fields to integers for consistency
    for vehicle in stock:
        try:
            vehicle["id"] = int(vehicle.get("id", 0))
        except (ValueError, TypeError):
            print("\nInvalid vehicle ID found "
                  "in stock data. Please check your sheet.")
            return None

    return stock


def require_stock_or_exit():
    """
    Retrieve the stock worksheet and its vehicle data.

    Returns:
        tuple: (sheet, stock)
            sheet (gspread.models.Worksheet or None):
            The stock worksheet, None if unavailable.
            stock (list[dict] or None): List of vehicle records,
            empty list if no stock, or None on error.

    Notes:
        - Prints user-friendly messages if the worksheet
          cannot be accessed or stock retrieval fails.
        - Distinguishes between empty stock and API errors.
    """
    # Attempt to access the 'stock' worksheet
    sheet = safe_sheet_call(SHEET.worksheet, "stock")
    if sheet is None:
        print(
            "\nUnable to access the stock worksheet. "
            "Check your internet/API connection."
        )
        return None, None

    # Attempt to get the current stock
    stock = get_stock(sheet)

    if stock is None:  # API error or invalid IDs
        print(
            "\nUnable to retrieve stock data. "
            "Please check your internet/API connection and try again."
        )
        return None, None

    # Return empty list if no vehicles in stock
    if not stock:
        return sheet, []

    return sheet, stock


def find_vehicle_by_id(stock, vehicle_id):
    """
    Find a vehicle in stock by its ID.

    Args:
        stock (list[dict]): The list of vehicle records.
        vehicle_id (int): The ID of the vehicle to search for.

    Returns:
        tuple: (vehicle, row_number)
            vehicle (dict or None): The vehicle record
             if found, otherwise None.
            row_number (int or None): The corresponding
            row number in the sheet, or None if not found.

    Notes:
        - Handles missing or malformed IDs safely.
        - Row numbers start at 2 to account for
          the header row in Google Sheets.
    """
    for index, vehicle in enumerate(stock, start=2):  # start=2 for header row
        try:
            vid = vehicle.get("id")
            if isinstance(vid, int) and vid == vehicle_id:
                return vehicle, index
        except (TypeError, ValueError):
            continue
    return None, None


def clear_screen():
    """
    Clear the terminal screen.
    Works on Windows, macOS, and Linux.
    """
    os.system("cls" if os.name == "nt" else "clear")


def get_required_input(prompt):
    """
    Prompt the user for input and prevent empty entries.

    Args:
        prompt (str): The message displayed to the user.

    Returns:
        str: A non-empty string entered by the user.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("This field cannot be empty. Please enter a value.")


def get_valid_year(prompt, min_year=2001, max_year=None):
    """
    Prompt the user for a year and validate it falls within a specified range.

    Args:
        prompt (str): The message to display to the user.
        min_year (int): Minimum allowable year (inclusive).
        max_year (int, optional): Maximum allowable year (inclusive).
        Defaults to 10 years in the future.

    Returns:
        int: A valid year entered by the user.
    """

    if max_year is None:
        max_year = date.today().year + 10  # allow 10 years into the future

    while True:
        try:
            year = int(input(prompt))
            if min_year <= year <= max_year:
                return year
            else:
                print(
                    f"\nPlease enter a valid year "
                    f" between {min_year} and {max_year}."
                )
        except ValueError:
            print("Invalid input. Please enter a numeric year.")


def get_valid_int(prompt, min_value=0):
    """
    Prompt the user for an integer greater than or equal to min_value.

    Args:
        prompt (str): The message displayed to the user.
        min_value (int, optional): Minimum allowable value (default is 0).

    Returns:
        int: A valid integer entered by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            else:
                print(
                    f"Please enter a number "
                    f"greater than or equal to {min_value}."
                )
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_valid_float(prompt, min_value=0):
    """
    Prompt the user for a float greater than or equal to min_value.

    Args:
        prompt (str): The message displayed to the user.
        min_value (float, optional): Minimum allowable value (default is 0).

    Returns:
        float: A valid float entered by the user.
    """
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
    Prompt the user for a UK vehicle registration number and validate it.
    Notes:
        - Validates format: AA21 ABC
        - Checks for duplicates in the stock.
    """
    while True:
        reg = (
            input("\nEnter vehicle registration number (e.g., CN18 YGG): ")
            .upper()
            .strip()
        )
        if not validate_registration(reg):
            print("\nInvalid registration format. "
                  "Please use the format AA12 ABC.")
            continue
        # Check if registration already exists
        if stock and any(v["reg_number"].upper() == reg for v in stock):
            print(
                "\nThis registration already exists in stock. "
                " Please enter a different one."
            )
            continue
        return reg


def get_user_choice():
    """
    Prompt the user to select an option from the main menu (1-4).

    Returns:
        int: The menu option selected by the user (1, 2, 3, or 4).
    """
    while True:
        choice = input("\nEnter your choice (1-4): ")
        if choice in ["1", "2", "3", "4"]:
            return int(choice)
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")


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
    Display all vehicles in stock in a neatly formatted table.

    Notes:
        - Truncates long text for readability in terminal.
        - Removes purchase price column to save width.
        - Handles empty stock gracefully.
    """
    sheet, stock = require_stock_or_exit()
    if not stock:
        print("\n*** No vehicles in stock ***\n")
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

    headers = [
        "ID",
        "Reg",
        "Make",
        "Model",
        "Year",
        "Mileage",
        "Price",
        "Status",
    ]

    # Max widths per column (mostly for very long text)
    max_widths = [4, 10, 10, 10, 4, 7, 8, 10]

    # Truncate only very long text
    table_data = [
        [
            str(cell)
            if isinstance(cell, (int, float))
            else (cell if len(cell) <= w else cell[: w - 3] + "...")
            for cell, w in zip(row, max_widths)
        ]
        for row in table_data
    ]

    # Print table
    print(tabulate(table_data, headers=headers, tablefmt="simple"))


def add_vehicle():
    """
    Appends the new vehicle to the stock worksheet and prints confirmation

    Notes:
        - Automatically assigns the next available vehicle ID.
        - Validates registration, year, mileage.
        - Collects purchase and sale price.
        - Appends the new vehicle to the
         Google Sheet and displays confirmation.
    """
    sheet, stock = require_stock_or_exit()
    if sheet is None:
        return

    # Determine next ID automatically based on existing stock,
    # ensuring we handle the case where stock is empty by defaulting to 1.
    next_id = max([v["id"] for v in stock], default=0) + 1

    reg_number = get_valid_registration(stock)

    make = get_required_input("\nEnter vehicle make (e.g., Ford): ").title()
    model = get_required_input("\nEnter "
                               "vehicle model (e.g., Fiesta): ").title()
    year = get_valid_year("\nEnter vehicle year (e.g., 2018): ")
    mileage = get_valid_int("\nEnter vehicle mileage  (e.g., 50000): ")
    purchase_price = get_valid_float("\nEnter "
                                     "vehicle purchase price (e.g., 8000): ")
    sale_price = get_valid_float("\nEnter vehicle sale price (e.g., 10000): ")

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

    if success is not None:  # <-- check result of API call
        print(f"\nVehicle {reg_number} added successfully!")
    else:
        print("\nFailed to add vehicle due to API error.")


def remove_vehicle():
    """
    Remove a vehicle from stock based on its ID.

    Returns:
        bool: True if at least one vehicle was removed, False otherwise.

    Features:
        - Prompts the user for a vehicle ID to remove.
        - Confirms removal before deleting.
    q   - Allows the user to cancel removal or try another ID if stock exists.
    """
    sheet, stock = require_stock_or_exit()
    if not stock:
        input("Press Enter to return to the main menu...")
        return False  # nothing removed

    vehicle_removed = False

    while True:
        user_input = input(
            "\nEnter vehicle ID to remove "
            "or press Enter to return to main menu: "
        ).strip()
        if user_input == "":
            break  # user chose to exit

        try:
            vehicle_id = int(user_input)
        except ValueError:
            print(
                "\nInvalid input. Please enter a valid numeric ID "
                "or press Enter to go back."
            )
            continue

        vehicle, row_number = find_vehicle_by_id(stock, vehicle_id)

        if not vehicle:
            print(f"\nVehicle ID {vehicle_id} not found. Please try again.")
            continue

        # Confirm removal
        confirm = (
            input(
                f"\nAre you sure you want to remove Vehicle ID {vehicle_id} "
                f"({vehicle['reg_number']})? (y/n): "
            )
            .strip()
            .lower()
        )

        if confirm == "y":
            success = safe_sheet_call(sheet.delete_rows, row_number)
            if success is not None:
                print(
                    f"\nVehicle ID {vehicle_id} "
                    f" ({vehicle['reg_number']}) removed successfully!"
                )
                vehicle_removed = True
            else:
                print("\nFailed to remove vehicle due to API error.")
            break  # exit after removal
        elif confirm == "n":
            print(
                "\nRemoval cancelled. You can try another "
                "vehicle ID or press Enter to return."
            )
            continue  # allow user to try another ID
        else:
            print("\nInvalid choice. Please enter 'y' or 'n'.")

    return vehicle_removed


def main():
    """
    Main program loop for Garage Stock Manager.

    Displays the main menu, handles user input, and calls
    relevant functions until the user chooses to exit.
    """
    while True:
        display_main_menu()
        choice = get_user_choice()

        if choice == 1:
            view_all_vehicles()
            input("\nPress Enter to return to the main menu...\n")
            clear_screen()

        elif choice == 2:
            clear_screen()
            add_vehicle()
            print("\nStock Updated:\n")
            view_all_vehicles()
            input("\nPress Enter to return to main menu...")
            clear_screen()

        elif choice == 3:
            clear_screen()
            view_all_vehicles()
            removed = remove_vehicle()  # True if a vehicle was removed
            if removed:
                print("\nStock Updated:\n")
                view_all_vehicles()  # show updated stock only if removed
                input("\nPress Enter to return to main menu...")
            clear_screen()  # always clear at the end

        elif choice == 4:
            print("\nExiting Garage Stock Manager. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
