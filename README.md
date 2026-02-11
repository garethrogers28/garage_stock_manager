# Garage Stock Manager
 
## Description

Garage Stock Manager is a command-line application designed to help manage vehicle inventory for a used car garage. It allows the user to view, add, and remove vehicles from a Google Sheets-based stock database.  This project was developed as Project 3 for the Code Institute Full Stack Developer Diploma and runs on their Mock terminal in Heroku.

link to live site - https://garage-stock-manager-b939d726e046.herokuapp.com/
 
## Business Goals/Visitor Goals

### 1. Efficient Inventory Management
   
Enable small used car garages to easily track and manage their vehicle stock without manual spreadsheets.

### 2. Reduce Errors in Stock Tracking
   
Prevent mistakes in recording vehicle details, prices, and status by enforcing validated inputs.

### 3. Improve Decision-Making

Provide garage owners with up-to-date stock data to assist in sales, pricing, and stock rotation decisions.

### 4. Scalable & Accessible Solution

Use cloud-based storage (Google Sheets) so multiple team members can access and update stock in real-time.


## User Stories 

### 1. View Vehicles

- As a garage owner, I want to view all vehicles in stock, so that I can quickly know which cars are available for sale.

### Acceptance Criteria:

- All vehicles are listed with ID, registration number, make, model, year, mileage, price, and status.

- If no vehicles exist, a friendly message informs the user.

### 2. Add Vehicles

- As a garage manager, I want to add new vehicles with details like make, model, year, mileage, and price, so that the stock is always up-to-date.

### Acceptance Criteria:

- Required fields cannot be empty.

- Year must be within a valid range (1975–2028).

- Mileage and prices must be numeric and non-negative.

- Vehicle is successfully added to the Google Sheet.

### 3. Remove Vehicles

- As a garage manager, I want to remove vehicles that are sold or no longer available, so that the stock list remains accurate.

### Acceptance Criteria:

- Only existing vehicle IDs can be removed.

- User must confirm deletion.

- Vehicle is removed from the Google Sheet successfully.

### 4. Data Validation

- As a garage owner, I want inputs like year, mileage, and price to be validated, so that incorrect data isn’t entered into the system.

### Acceptance Criteria:

- Invalid inputs prompt the user to re-enter values.

- The system does not accept empty or malformed entries.

### 5. Cloud Storage (Google Sheets)

- As a garage manager, I want the stock data to be stored in Google Sheets, so that it can be accessed and updated from any device with internet access.
  
Acceptance Criteria:

- All stock changes (add/remove) are immediately reflected in the Google Sheet.

- Data persists between sessions.

### 6. Handle API Failures

- As a garage manager, I want to be notified if the system cannot access the stock data, so that I understand why the application isn’t working and can take appropriate action.

### Acceptance Criteria:

- If the Google Sheets API call fails, a clear, user-friendly message is displayed.

- The application does not crash or lose existing data.

- Users are guided on next steps (e.g., “Please check your internet connection or API credentials and try again”).


# Design

## Flowchart


## Wireframes

- Command-line interface uses system defaults 

## Existing Features

### 1. Menu-Driven Interface
- Simple and user-friendly command-line menu with four clear options.

### 2. View All Vehicles
- Displays a formatted list with:

 - Vehicle ID, Registration Number, Make, Model, Year, Mileage, Purchase Price, Sale Price, Status

### 3. Add a Vehicle

- Automatic ID generation

- Input validation (year, mileage, price)

- Automatic status set to "For Sale"

- Automatic date added

### 4. Remove a Vehicle

- Select vehicle by ID

- Confirmation prompt before deletion

- Prevents accidental removal

- Error message if vehicle ID not found

### 5. Google Sheets Integration

- Uses Google Sheets as a cloud-based database

- Real-time data storage and retrieval

- Persistent data (data saved outside the program)

### 6. Error Handling

- Handles Google Sheets API connection errors

- Prevents crashes due to invalid data

- User-friendly error messages

### 7. Data Validation & Sanitisation

- Prevents empty inputs

- Ensures numeric fields are valid

- Enforces valid year range

- Standardises text formatting (e.g., uppercase registration, title-case make/model)

### 8. Continuous Program Loop

- Returns to the main menu after each action

- Runs until the user chooses to exit


## Future Features 


# Technologies used 

## Programming Language

- Python 3
Core language used to develop the application logic, user interface, and data handling.

## Libraries & Frameworks

- gspread
Python library used to interact with Google Sheets for reading, writing, and updating stock data.

- google-auth (google.oauth2.service_account)
Used to securely authenticate and authorise access to the Google Sheets API via service account credentials.

- datetime (Python Standard Library)
Used to automatically generate and store the date a vehicle is added to stock.

## External Services

- Google Sheets API
Used as a cloud-based database to store vehicle inventory data.

- Google Cloud Platform (GCP)
Used to create and manage service account credentials for API authentication.



## How to View the Project

1. Clone the repository

2. Install dependencies (pip install -r requirements.txt)

3. Add your creds.json for Google Sheets API access

4. Run the application

# Testing


## User Story testing
                                                                                                    |        |                          
                                                                                
## Manual testing 


## Bugs


 
## IDE

- Visual Studio Code 

## Version Control 

- Github

- link to repository  https://github.com/garethrogers28/garage_stock_manager

## Deployment

- The project was deployed using Code Institute's Heroku mock terminal.
- The following steps were followed during deployment:
  
1. Cloning this repository
  
2. Creating a new Heroku app for the project
 
3. Add buildpacks for Python first and then for Node Js
  
4. Creating a Config Var called PORT with a value of 8000
   
5. Link the Heroku app to the repository
 
6. Finally deploy by clicking Deploy


## Credits

- Code institute for the deployment process and deployment terminal

## Content 

- I created the database on google sheets 
