# Garage Stock Manager
 
# Description

- Garage Stock Manager is a command-line application designed to help manage vehicle inventory for a used car garage. It allows the user to view, add, and remove vehicles from a Google Sheets-based stock database. This project was developed as Project 3 for the Code Institute Full Stack Developer Diploma.
 
# Visitor Goals



# Business Goals

Efficient Inventory Management
- Enable small used car garages to easily track and manage their vehicle stock without manual spreadsheets.

Reduce Errors in Stock Tracking
- Prevent mistakes in recording vehicle details, prices, and status by enforcing validated inputs.

Improve Decision-Making
- Provide garage owners with up-to-date stock data to assist in sales, pricing, and stock rotation decisions.

Scalable & Accessible Solution
- Use cloud-based storage (Google Sheets) so multiple team members can access and update stock in real-time.


# User Stories 

## View Vehicles

- As a garage owner, I want to view all vehicles in stock, so that I can quickly know which cars are available for sale.

Acceptance Criteria:

- All vehicles are listed with ID, registration number, make, model, year, mileage, price, and status.

- If no vehicles exist, a friendly message informs the user.

## Add Vehicles

- As a garage manager, I want to add new vehicles with details like make, model, year, mileage, and price, so that the stock is always up-to-date.

Acceptance Criteria:

- Required fields cannot be empty.

- Year must be within a valid range (1975–2028).

- Mileage and prices must be numeric and non-negative.

- Vehicle is successfully added to the Google Sheet.

## Remove Vehicles

- As a garage manager, I want to remove vehicles that are sold or no longer available, so that the stock list remains accurate.

Acceptance Criteria:

- Only existing vehicle IDs can be removed.

- User must confirm deletion.

- Vehicle is removed from the Google Sheet successfully.

## Data Validation

- As a garage owner, I want inputs like year, mileage, and price to be validated, so that incorrect data isn’t entered into the system.

Acceptance Criteria:

- Invalid inputs prompt the user to re-enter values.

- The system does not accept empty or malformed entries.

## Cloud Storage (Google Sheets)

- As a garage manager, I want the stock data to be stored in Google Sheets, so that it can be accessed and updated from any device with internet access.
  
Acceptance Criteria:

- All stock changes (add/remove) are immediately reflected in the Google Sheet.

- Data persists between sessions.

## Handle API Failures

- As a garage manager, I want to be notified if the system cannot access the stock data, so that I understand why the application isn’t working and can take appropriate action.

Acceptance Criteria:

- If the Google Sheets API call fails, a clear, user-friendly message is displayed.

- The application does not crash or lose existing data.

- Users are guided on next steps (e.g., “Please check your internet connection or API credentials and try again”).


# Design


## Wireframes




## Colours



## Fonts



# Existing Features

## Menu-Driven Interface
- Simple and user-friendly command-line menu with four clear options.

## View All Vehicles
- Displays a formatted list of all vehicles currently in stock, including:

- Vehicle ID

- Registration number

- Make and model

- Year

- Mileage

- Purchase price

- Sale price

- Status

## Add a Vehicle
- Allows users to add a new vehicle to stock with:

- Automatic ID generation

- Input validation for required fields

- Year range validation

- Numeric validation for mileage and pricing

- Automatic status set to "For Sale"

- Automatic date added

## Remove a Vehicle

- Select vehicle by ID

- Confirmation prompt before deletion

- Prevents accidental removal

- Displays error if vehicle ID is not found

## Google Sheets Integration

- Uses Google Sheets as a cloud-based database

- Real-time data storage and retrieval

- Persistent data (data saved outside the program)

## Error Handling

- Handles Google Sheets API connection errors

- Prevents crashes due to invalid data

- ser-friendly error messages

## Data Validation & Sanitisation

- Prevents empty inputs

- Ensures numeric fields are valid

- Enforces valid year range

- Standardises text formatting (e.g., uppercase registration, title-case make/model)

## Continuous Program Loop

- Returns to the main menu after each action

- Runs until the user chooses to exit


## Future Features 


## Technologies used 



## How to View the Project



# Testing

## Responsiveness




## User Story testing
                                                                                                    |        |                          

                                                                                
## Manual testing 


## Validator Testing


## Lighthouse Testing 



## Bugs


 
## IDE



## Version Control 



## Deployment



## Credits


## Content 

