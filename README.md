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

1. As a garage owner, I want to view all vehicles in stock, so that I can quickly know which cars are available for sale.

2. As a garage manager, I want to add new vehicles with details like make, model, year, mileage, and price, so that the stock is always up-to-date.
 
3. As a garage manager, I want to remove vehicles that are sold or no longer available, so that the stock list remains accurate.

4. As a garage owner, I want inputs like year, mileage, and price to be validated, so that incorrect data isn’t entered into the system.
 
5. As a garage manager, I want the stock data to be stored in Google Sheets, so that it can be accessed and updated from any device with internet access.

6. As a garage manager, I want to be notified if the system cannot access the stock data, so that I understand why the application isn’t working and can take appropriate action.

# Design

- Note: Since the application runs in the terminal, there is no design of the user interface as such.

The deployed application runs in a mock terminal on Heroku in order to demonstrate the project, the design of the mock terminal is built into the template provided by Code Institute.

## Flowchart


## Wireframes

- Command-line interface uses system defaults 

## Existing Features

### 1. Menu-Driven Interface

- Simple and user-friendly command-line menu with four clear options. The user is given a welcome message and given options to View Vehicles, Add Vehicle, Remove Vehicle and Exit.

<img width="728" height="406" alt="home-page-welcome" src="https://github.com/user-attachments/assets/aa70ace1-e80a-4aa7-829c-c725de1d0c48" />


### 2. View All Vehicles

- Displays a table to the user with:

 - Vehicle ID, Registration Number, Make, Model, Year, Mileage, Sale Price, Status. This is fantastic for the user to see all available stock in a user friendly table using Tabulate.

<img width="723" height="401" alt="View-all-vehicles" src="https://github.com/user-attachments/assets/9a2966a1-5c44-452f-b36e-9c43867700b3" />


### 3. Add a Vehicle

- Input validation for Registration using regex

<img width="724" height="408" alt="validate-ukreg-number" src="https://github.com/user-attachments/assets/f64412d5-d7de-48c1-8443-4708c7cd8af7" />

- Automatic ID generation. The user does not have to have give the vehicle an ID as this will be applied automatically depending on the next available space in the file.

- Input validation (year, mileage, purchase price, sale price). The user must enter a number for mileage, purchase and sale prices. They must enter years between 2001 and 2036 or they will get feedback asking them to enter a valid number.

<img width="722" height="407" alt="validate-mileage" src="https://github.com/user-attachments/assets/603c952a-b02a-4b06-a5c0-07d67559eeab" />
<img width="719" height="178" alt="validate-purchase-price-int" src="https://github.com/user-attachments/assets/77da12c2-45e7-4729-ab6e-ebb25de69f2d" />
<img width="726" height="170" alt="validate-sale-price-int" src="https://github.com/user-attachments/assets/dc3c6ade-9976-4b24-adaa-d240d3c5661f" />

- Automatic status set to "For Sale". The user does not have to enter the status which streamlines the process for the user. 

- Automatic date added. The user does not havce to enter the date that the vehicle was added. This is great again to save time for the user and eradicates any manual error.

- Confirmation of vehicle added with updated stock table

<img width="727" height="410" alt="add-vehicle-success" src="https://github.com/user-attachments/assets/d48ea171-b0eb-44a0-be7c-1e05d13783f2" />

- User can go direclty back to main mernu after veiwing the revised stock table

<img width="731" height="410" alt="updated-stock-return-menu" src="https://github.com/user-attachments/assets/a9d295d3-5b79-4f22-8f0f-2b22b51902a5" />


### 4. Remove a Vehicle

- View all Vehicles. The user is first given the list of vehicles (same as view all vehicles)

- Select vehicle by ID. The user is asked to enter a Vehicle ID that they wish to remove. This reduces input for the user so they do not have to type in the full details.

 <img width="731" height="413" alt="remove-vehicle-stock-list" src="https://github.com/user-attachments/assets/c4d426bd-468a-4b77-b040-a10d702d06a8" />

- Confirmation prompt before deletion. Once the user has chosen the ID, Garage Stock Manager will prompt the user to confirm they are sure that they want to delete. This Prevents accidental removal

 <img width="731" height="415" alt="removal-confirmation-update-stock" src="https://github.com/user-attachments/assets/a0404f33-d3b7-481d-b150-e1d4c5c6bc17" />

- Error message if vehicle ID not found. If the user enters an ID that is not available. The user will be asked to review the list and try again.

<img width="720" height="411" alt="remove-vehicle-no-id-found" src="https://github.com/user-attachments/assets/d9c77965-eaa0-42d1-bd5e-4a1c980f13ba" />


### 5. Google Sheets Integration

- Uses Google Sheets as a cloud-based database. 

- Real-time data storage and retrieval. The user does not have to manually edit and save their spreadsheet/file. 

- Persistent data (data saved outside the program)

### 6. Error Handling

- Handles Google Sheets API connection errors. If for some reason the API is not working = down the user will be infomred at the earliest possible opportunity instead of making them go all the way to the end of the program.

- Prevents crashes due to invalid data

- User-friendly error messages. The user is always prompted what went wrong if they enter incorrect data. This is brilliant for the user to alwasy be kept informed of their actions so they do not get lost.

### 7. Data Validation & Sanitisation

- Prevents empty inputs. The user is unable to enter empty data ensuring all data is captured.

- Ensures numeric fields are valid

- Enforces valid year range

- Standardises text formatting (e.g., uppercase registration, title-case make/model)

### 8. Continuous Program Loop

- Returns to the main menu after each action. The user can perfom multiple tasks in one session so they do not have to re run the program all the time. 

- Runs until the user chooses to exit


## Future Features 

- Edit Vehicle function can be added such as sale price and mileage.

- Search for Vehicle by registration, make or year/price range.

- Audit Trail to record sale prices and previous vehicle details.

- a Profit section could be implemented using purchase and sold price once the sold price has been recorded. Creating new data for the user to benefit from. 

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

- https://garage-stock-manager-b939d726e046.herokuapp.com/

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
