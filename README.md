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

1. View Vehicles

- As a garage owner, I want to view all vehicles in stock, so that I can quickly know which cars are available for sale.

Acceptance Criteria:

All vehicles are listed with ID, registration number, make, model, year, mileage, price, and status.

If no vehicles exist, a friendly message informs the user.

2. Add Vehicles

- As a garage manager, I want to add new vehicles with details like make, model, year, mileage, and price, so that the stock is always up-to-date.

Acceptance Criteria:

- Required fields cannot be empty.

- Year must be within a valid range (1975–2028).

- Mileage and prices must be numeric and non-negative.

- Vehicle is successfully added to the Google Sheet.

3. Remove Vehicles

- As a garage manager, I want to remove vehicles that are sold or no longer available, so that the stock list remains accurate.

Acceptance Criteria:

- Only existing vehicle IDs can be removed.

- User must confirm deletion.

- Vehicle is removed from the Google Sheet successfully.

4. Data Validation

- As a garage owner, I want inputs like year, mileage, and price to be validated, so that incorrect data isn’t entered into the system.

Acceptance Criteria:

- Invalid inputs prompt the user to re-enter values.

- The system does not accept empty or malformed entries.

5. Cloud Storage (Google Sheets)

- As a garage manager, I want the stock data to be stored in Google Sheets, so that it can be accessed and updated from any device with internet access.
  
Acceptance Criteria:

- All stock changes (add/remove) are immediately reflected in the Google Sheet.

- Data persists between sessions.

6. Handle API Failures

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

- View all vehicles in stock with details such as registration number, make, model, year, mileage, price, and status.
- Add a vehicle to the stock with validation for all fields (year, mileage, purchase/sale price).
- Remove a vehicle by ID with confirmation prompt.
- Google Sheets integration for storing and retrieving stock data in real-time.


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

