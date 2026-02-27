# Garage Stock Manager


## Table of Contents

- [Description](#description)
- [Business Goals](#business-goals)
- [User Stories](#user-stories)
- [Scope](#scope)
- [Design](#design)
- [Features](#existing-features)
- [Future Features](#future-features)
- [Data Model](#data-model)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Bugs](#bugs)
- [Installation & Local Development](#installation--local-development)
- [Deployment](#deployment)
- [Limitations](#limitations)
- [Credits](#credits)


## Description

Garage Stock Manager is a command-line application designed to help manage vehicle inventory for a used car garage. It allows the user to view, add, and remove vehicles from a Google Sheets-based stock database. The system was built using Python and integrates with the Google Sheets API to provide real-time data storage and retrieval. It focuses on simplicity, reliability, and data accuracy through structured validation and defensive programming techniques.

This project was developed as Project 3 for the Code Institute Full Stack Developer Diploma and runs on their Mock terminal in Heroku.

link to live site - https://garage-stock-manager-b939d726e046.herokuapp.com/

link to repository  https://github.com/garethrogers28/garage_stock_manager
 
## Business Goals

1. Efficient Inventory Management
   
Enable small used car garages to easily track and manage their vehicle stock without manual spreadsheets.

2. Reduce Errors in Stock Tracking
   
Prevent mistakes in recording vehicle details, prices, and status by enforcing validated inputs.

3. Improve Decision-Making

Provide garage owners with up-to-date stock data to assist in sales, pricing, and stock rotation decisions.

4. Scalable & Accessible Solution

Use cloud-based storage (Google Sheets) so multiple team members can access and update stock in real-time.


## User Stories 

1. As a garage owner, I want to view all vehicles in stock, so that I can quickly know which cars are available for sale.

2. As a garage manager, I want to add new vehicles with details like make, model, year, mileage, and price, so that the stock is always up-to-date.
 
3. As a garage manager, I want to remove vehicles that are sold or no longer available, so that the stock list remains accurate.

4. As a garage owner, I want inputs like registration, year, mileage, and price to be validated, so that incorrect data isn’t entered into the system.
 
5. As a garage manager, I want the stock data to be stored in Google Sheets, so that it can be accessed and updated from any device with internet access.

6. As a garage manager, I want to be notified if the system cannot access the stock data, so that I understand why the application isn’t working and can take appropriate action.

## Scope

The scope of Garage Stock Manager was to develop a terminal-based inventory management system for small independent garages. The focus was on building a functional backend application that integrates with the Google Sheets API to manage live stock data.

### In Scope

The following features were included within the project scope:

- Viewing all vehicles currently in stock

- Adding new vehicles with full input validation

- Removing vehicles with confirmation prompts

- Automatic ID, status, and date generation

- Prevention of duplicate registrations

- Defensive programming and error handling

- Integration with Google Sheets for persistent cloud storage

The application prioritises data integrity, usability within a command-line interface, and reliable API communication.

### Out Of Scope

The following features were considered beyond the scope of this project:

- Editing existing vehicle records (e.g., updating mileage, purchase price, or sale price).

- Advanced search functionality (e.g., searching by registration, make, model, year range, or price range).

- Audit trail functionality to track historical changes, sale prices, and previous vehicle details.

- Profit calculation and reporting based on purchase and final sale price.

- Expansion of the system to support broader small business inventory management beyond vehicle stock.

These features could be implemented in future iterations but were not required for the current project objectives.

### CRUD Functionality

The application implements three of the four core CRUD operations:

- Create (Add Vehicle)
- Read (View Vehicles)
- Delete (Remove Vehicle)

Update functionality is planned for future development.

## Design

- Note: Since the application runs in the terminal, there is no design of the user interface as such.

- The deployed application runs in a mock terminal on Heroku in order to demonstrate the project, the design of the mock terminal is built into the template provided by Code Institute.

## Flowchart

The flowchart was initially designed in Lucidchart and finalised using Inkscape.

<img width="1822" height="1563" alt="Flowcharts" src="https://github.com/user-attachments/assets/bba3c3bb-e752-4877-96e6-0ba33103a1a0" />

Here is the link to lucidchart

- https://lucid.app/lucidchart/a798661a-fe63-45a9-876b-07ff947f5c8d/edit?viewport_loc=-9380%2C-4962%2C3626%2C1736%2C0_0&invitationId=inv_f127bb38-9463-474d-9fbc-592348816baa


## Wireframes

- Command-line interface uses system defaults 

## Existing Features

### 1. Menu-Driven Interface

- Simple and user-friendly command-line menu with four clear options. The user is given a welcome message and given options to View Vehicles, Add Vehicle, Remove Vehicle and Exit.

<img width="719" height="406" alt="menu-screen" src="https://github.com/user-attachments/assets/20616055-d18a-4f64-a1b7-a65801f29824" />


### 2. View All Vehicles

- Displays a table to the user with:

- Vehicle ID, Registration Number, Make, Model, Year, Mileage, Sale Price, Status. This improves readability and enhances user experience.

<img width="725" height="408" alt="view-all-vehicles" src="https://github.com/user-attachments/assets/7145f6b1-994a-44dc-b750-709b5bca3cd0" />


- Pressing Enter takes the user back to the main menu and clears the screen to keep the terminal clean. 

### 3. Add a Vehicle

- Users can add a vehicle. The system will ask them for all vehicles details such as Registration Number, Make, Model, Year, Mileage, Purchase Price and Sale Price. They will receive a success message when complete confirming Reg number and also be informed of the stock updating.

<img width="722" height="409" alt="add-vehicle" src="https://github.com/user-attachments/assets/487a2a7a-9c84-4299-b440-f0ced0159ac3" />

- Automatic ID and date generation. The user does not have to have give the vehicle an ID or date as this will be applied automatically depending on the next available space in the file. This reduces manual error and improves efficiency.

- Automatic status set to "For Sale". The user does not have to enter the status which streamlines the process for the user. 

- User can go directly back to main menu after viewing the revised stock table.

### 4. Remove a Vehicle

- View all Vehicles. The user is first given the list of vehicles (same as view all vehicles)

- Select vehicle by ID. The user is asked to enter a Vehicle ID that they wish to remove. This reduces input for the user so they do not have to type in the full details. 

- Confirmation prompt before deletion. Once the user has chosen the ID, Garage Stock Manager will prompt the user to confirm they are sure that they want to delete. This Prevents accidental removal

 <img width="723" height="411" alt="remove-vehicle" src="https://github.com/user-attachments/assets/9ceec4ed-2836-417a-a242-dcc103e06749" />


- Error message if vehicle ID not found. If the user enters an ID that is not available. The user will be asked to review the list and try again.

- The user will then be shown an updated stock table containing the new entry so they can see the new vehicle details.

### 5. Google Sheets Integration

- Uses Google Sheets as a cloud-based database. 

- Real-time data storage and retrieval. The user does not have to manually edit and save their spreadsheet/file. 

- Persistent data (data saved outside the program)

### 6. Error Handling

- Handles Google Sheets API connection errors. If for some reason the API is not working, the user will be informed at the earliest possible opportunity instead of making them go all the way to the end of the program.
  
<img width="727" height="408" alt="api-error" src="https://github.com/user-attachments/assets/d2e18e9c-a25b-427d-bd2d-e5f3cd8d9905" />


- Prevents crashes due to invalid data

- User-friendly error messages. The user is always prompted what went wrong if they enter incorrect data. This ensures the user is always informed of their actions and understands how to correct errors.

- sheet_errors.log stores all errors

### 7. Data Validation & Sanitisation

- Input validation (reg, year, mileage, purchase price, sale price). The user must enter a number for mileage, purchase and both prices.
 
- Vehicle registration numbers are validated using Regular Expressions (regex). The program ensures that registrations follow the UK 2001+ format: AB12 ABC

- The program also converts user input to uppercase before validation.
  
- User must enter years between 2001 and 2036 or they will get feedback asking them to enter a valid year between 2001 and 2036.
  
Note
The garage has no interest in selling cars that are over 25 years old which is why I have chosen 2001 as the oldest date. This also means the system did not need to check for older version registration numbers. 

<img width="722" height="409" alt="validation" src="https://github.com/user-attachments/assets/549175e0-401f-46b2-9a69-c1b8a879f7fd" />

- Prevents empty inputs. The user is unable to enter empty data ensuring all data is captured.
  

### 8. Continuous Program Loop

- Returns to the main menu after each action. The user can perform multiple tasks in one session so they do not have to re run the program all the time. 

- Runs until the user chooses to exit

## Future Features 

- Edit Vehicle function can be added so the user can edit things like mileage and purchase price. Incase the car is not selling or if work has been done on a vehicle that increases the sale price.

- Search for Vehicle by registration, make, model, year range or price range.

- A sell vehicle function that applies the 'Sold' status and records the 'sold price'.

- Audit Trail to record sale prices and previous vehicle details.

- Profit section could be implemented using purchase and sold price once the sold price has been recorded. Creating new data for the user to benefit from. 

- Garage Stock manager can be edited to suit any small business that requires to store data not just car garages.

## Data Model

- Google Sheet

| Column         | Description                                 |
|----------------|---------------------------------------------|
| id             | Auto-incremented unique vehicle ID          |
| reg_number     | vehicle registration (UK format, validated) |
| make           | Vehicle make (title-case)                   |
| model          | Vehicle model (title-case)                  |
| year           | Vehicle year (validated)                    |
| mileage        | Vehicle mileage (numeric)                   |
| purchase_price | Purchase price of vehicle (numeric)         |
| sale_price     | Sale price of vehicle (numeric)             |
| status         | Vehicle status (default: For Sale)          |
| date_added     | Date the vehicle was added                  |

- Garage Stock Manager uses a single Google Sheets worksheet (stock) as its database. Each row in the sheet represents one vehicle in the garage inventory.The system follows a simple single-entity data model, where all vehicle information is stored in structured columns.
  
- All operations (view, add, remove) interact directly with the stock worksheet. 

A single-table structure was chosen because:

- The application is small and focused on stock management.

- It simplifies CRUD operations.

- Google Sheets acts as a lightweight cloud database.

- No complex relational data is required.

This design keeps the system efficient, easy to maintain, and suitable for a command-line application.

## Technologies used 

## Programming Language

- Python 3
Core language used to develop the application logic, user interface, and data handling.

Note: HTML, CSS and Javascript exist in the template provided by Code Institute for this project but these are to run the mock terminal. The program itself is built purely using Python.

## Python Library Dependencies and Packages

- gspread
Used to interact with Google Sheets for reading, writing, and updating stock data.

- google-auth (google.oauth2.service_account)
Used to securely authenticate and authorise access to the Google Sheets API via service account credentials.

- tabulate
  used to display data into a nice table for better UX

## Built-in Python Modules

-  datetime
Used to automatically generate and store the date a vehicle is added to stock.  

- re
  used to validate registration numbers

- os
  used to clear terminal screen for user

## External Services

- Google Sheets API
Used as a cloud-based database to store vehicle inventory data.

- Google Cloud Platform (GCP)
Used to create and manage service account credentials for API authentication.

## How to View the Project

- https://garage-stock-manager-b939d726e046.herokuapp.com/

# Testing

Throughout the Build phase Python Tutor, PEP8 Online and Chrome Developer Tools are used to ensure the application works as expected. The app was tested on Chrome and Edge browsers. Testing was conducted throughout development to ensure functionality, reliability, and data integrity. Both manual testing and user story validation were performed to confirm that all core features met their intended objectives.

When assessing pep8 validation there were no erros or warnings  

- run.py - 0 Errors / 0 Warnings

## User Story testing

| User Story                                                                                                                                                                        | Result |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| 1. As a garage owner, I want to view all vehicles in stock, so that I can quickly know which cars are available for sale.                                                         | Pass   |
| 2. As a garage manager, I want to add new vehicles with details like make, model, year, mileage, and price, so that the stock is always up-to-date.                               | Pass   |
| 3. As a garage manager, I want to remove vehicles that are sold or no longer available, so that the stock list remains accurate.                                                  | Pass   |
| 4. As a garage owner, I want inputs like registration, year, mileage, and price to be validated, so that incorrect data isn’t entered into the system.                            | Pass   |
| 5. As a garage manager, I want the stock data to be stored in Google Sheets, so that it can be accessed and updated from any device with internet access.                         | Pass   |
| 6. As a garage manager, I want to be notified if the system cannot access the stock data, so that I understand why the application isn’t working and can take appropriate action. | Pass   |                                                                                                                             
                                                                                
## Manual testing 

| Feature                             | Steps                                                                                                | Expected Outcome                                                                                                                                                                           | Outcome |
|-------------------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Menu Screen                         | User Opens App                                                                                       | Welcome message is displayed along with 4 options. View Vehicles, Add Vehicle, Remove Vehicle and Exit                                                                                     | Pass    |
| View All Vehicles                   | User chooses option 1 from menu                                                                      | All vehicles displayed in a table using tabulate. Table displays ID, Reg, Make, Model, Year, Mileage and Sale Price.                                                                       | Pass    |
| Validate menu input                 | User chooses option that is not 1 to 4 or enters no option                                           | Invalid choice. Please enter a number between 1 and 4 is displayed to the user                                                                                                             | Pass    |
| Add Vehicle                         | User chooses option 2 from menu                                                                      | User is prompted to enter all vehicle details such as Registration, Make, Model, Year, Mileage, Purchase Price and Sale Price                                                              | Pass    |
| Validate Registration               | User types in Registration that doesn't match uk format or enters a registration that is already used | User is informed they have 'entered invalid format and prompted to enter Registration in UK format (AB97 LOL) or This registration already exists in stock.  Please enter a different one' | Pass    |
| Validate Year                       | User tries to enter a year that is not in between 2001 and 2036                                      | User is given feedback - 'Please enter a valid year between 2001 and 2036.'                                                                                                                | Pass    |
| Auto ID, Status and Date            | User successfully adds a vehicle                                                                     | The ID, Status (for sale) and date are automatically added to Google sheets.                                                                                                           | Pass    |
| Confirmation of Success             | User successfully adds a vehicle                                                                     | The user is given feedback of 'latest vehicle added such as Vehicle VB12 GHG added successfully!'                                                                                          | Pass    |
| Stock Updated after adding vehicle  | User successfully adds a vehicle                                                                     | The stock table updates so the user can see the updated stock table                                                                                                                        | Pass    |
| Return to main menu                 | When user is offered the chance to go back to main menu and presses enter                            | The screen clears and user is sent back to main menu with all 4 options again                                                                                                              | Pass    |
| Remove Vehicle                      | User selects option 3 to remove vehicle                                                              | User is shown all vehicles in a table and is then prompted to enter ID of vehicle they wish to remove                                                                                      | Pass    |
| Validate ID                         | When removing a vehicle the user selects an ID that does not exist                                   | The user is prompted with 'Vehicle ID 12 not found. Please try again.'                                                                                                                     | Pass    |
| Confirm/Cancel removal              | The user enters matching ID to remove vehicle so vehicle is found                                    | User is asked if they are sure they wish to remove with simple y/n options. Option to select another ID if they choose n.                                                                  | Pass    |
| Removal Successful                  | The user chooses Y when confirming that they wish to remove vehicle                                  | User is given confirmation feedback of removed vehicle 'Vehicle ID 11  (VB12 GHG) removed successfully!' ID and Reg number are displayed along with an updated table of the latest stock   | Pass    |
| Exit                                | The user selects option 4                                                                            | User is logged out of Garage Stock Manager                                                                                                                                                 | Pass    |
| API Error Handling                  | Disconnect from internet or remove service account                                                   | User sees a clear message: 'Unable to access the stock worksheet. Please ensure the Google Sheet exists and the service account has permission.'                                           | Pass    |
| Empty Input Validation              | User presses Enter without entering a value for required field                                       | System prompts user to enter a value until valid input is provided                                                                                                                         |     Pass    |
| Invalid Numeric Input               | User enters letters instead of numbers for Year, Mileage, Purchase or Sale Price                     | System prompts: 'Invalid input. Please enter a numeric value.'                                                                                                                             |   Pass      |


## Bugs

- Registration Validation

Before implementing registration validation, the system allowed duplicate or malformed registration numbers. This caused potential bugs such as duplicate vehicle entries, inconsistent IDs, and confusing stock listings. After adding get_valid_registration() and the regex check, these issues were prevented, and the system became more reliable.

- Tabulate overflowing table

When using tabulate, I struggled to ensure the table did not overflow onto separate lines. Whilst the data displayed well in the terminal, it did not display neatly when deployed to Heroku. I was having issues with column truncation. I decided it was more important for the user to see the Sale Price rather than the Purchase Price, so I removed the purchase price column to maintain a clean layout.

- Duplicating api error messages
 
When the Google Sheet API is inaccessible, some functions may display the error message twice. This does not affect functionality; user-friendly messages still guide the user and prevent crashes. This project strengthened my understanding of defensive programming principles.

 
## IDE

- Visual Studio Code 

## Version Control 

- Git was used to track and manage changes throughout development.

- Frequent commits were made with meaningful commit messages describing features, bug fixes, and refactoring.

- The repository was regularly pushed to GitHub to ensure code was safely stored and versioned.

## Deployment

This project was deployed using the Code Institute Heroku mock terminal

### Heroku Deployment Steps

Note

The requirements.txt file in the IDE must be updated to package all dependencies. To do this:

- Enter the following into the terminal: 'pip3 freeze > requirements.txt'
- Commit the changes and push to GitHub
  
Next, follow the steps below:

1. Login to Heroku, create an account if necessary
2. Once at your Dashboard, click 'Create New App'
3. Enter a name for your application, this must be unique, and select a region
4. Click 'Create App'
5. At the Application Configuration page, apply the following to the Settings and Deploy sections:
6. Within 'Settings', scroll down to the Config Vars section to apply the credentials being used by the application. In the Reveal Config Vars enter 'CREDS' for the Key field and paste the all the contents from the creds.json file into the Value field
7. Click 'Add'
8. Add another Config Var with the Key of 'PORT' and the Value of '8000'
9. Within Settings, scroll down to the Buildpacks sections, click to Add a Buildpack
10. Select Python from the pop-up window and Save
11. Add the Node.js Buildpack using the same method
12. Navigate to the Deploy section, select Github as the deployment method, and connect to GitHub when prompted
13. Use your GitHub repository name created for this project
14. Finally, scroll down to and select to deploy manually or automatically depending on your choice. I deployed manually on ths occasion. 

### Installation & Local Development

1. The project was created by cloning the Code Institute Python template repository.

- git clone https://github.com/garethrogers28/garage_stock_manager.git

2. Navigate into the project directory

- cd garage_stock_manager

3. Install required dependencies:

- pip install -r requirements.txt

4. Create a creds.json file with your Google Service Account credentials.
 
5. Run application python3 run.py

### Limitations

- The application requires an active internet connection to access the Google Sheets database.

- If the Google Sheets API is unavailable, core functionality (viewing, adding, removing vehicles) will be temporarily restricted.

- The application does not include user authentication or role-based access control.

- The system uses a single Google Sheets worksheet, meaning it is not designed for complex relational data structures.

- As a command-line application, it does not include a graphical user interface.

### Security

- Sensitive credentials such as the Google Sheets service account file were excluded from the repository and stored securely using Heroku Config Vars.

- The project follows best practices by preventing exposure of API keys and authentication data.

## Credits

### People

- Code Institute Full Stack Developer software course.
- Mentor Brian Macharia for guiding and advising throughout the projects lifecycle on how to improve UX and my code.
- Code institute for the deployment process and deployment terminal.

### Software & Web Applications

- Stack overflow for general question troubleshooting.
- Chatgpt (especially for understanding api error handling and how to replicate an api error).
- Ruff for code formatting (although this still required manual editing to ensure no errors).
- Lucidchart for the flowchart
- PEP8 Validator for validating Python code
- Python Tutor for testing sections of code 

## Content 

- I created the database on Google Sheets
