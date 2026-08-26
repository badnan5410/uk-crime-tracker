# UK Crime Tracker

A desktop application for exploring and understanding local crime data across the UK by postcode.

## Status

🚧 Currently in development.

Stage 3 — API integration and crime data retrieval — is complete.

Development is currently in Stage 4: data processing, exploration, and visualisation.

Stage 4a — the Overview page — is complete.

Stage 4b — the View Crimes page — is complete, allowing individual Police API crime records to be explored and filtered by crime category.

Stage 4c — the Categories page — is now in development. Crime category data is processed and visualised using a dynamically generated Matplotlib horizontal bar chart embedded directly within the PyQt5 interface.

## Current Features

- Desktop interface built with PyQt5
- Multi-page application navigation
- UK postcode search and validation
- Postcode location and coordinate retrieval using Postcodes.io
- Street-level crime data retrieval using the UK Police Data API
- Crime searches based on postcode latitude and longitude
- Two-stage API search and validation flow
- API error and exception handling
- User-facing API error messages
- Geographic and crime data passed into the results interface
- Dynamic results refresh when new search data is received

### Crime Data Processing

- Crime record processing and aggregation
- Total recorded crime calculation
- Most common crime category calculation
- Crime category frequency calculation
- Human-readable crime category formatting
- Human-readable reporting month and year formatting
- Crime records filtered dynamically by category
- Available police outcome information extracted from individual records
- Missing outcome information handled as unresolved
- Crime category data prepared for visualisation

### Overview Page

- Dynamic display of:
  - searched postcode
  - district and region
  - reporting month and year
  - total recorded crimes
  - most common crime category
  - number of reports for the most common category
- Information explaining approximate and anonymised crime locations

### View Crimes Page

- Browse individual crime records
- Filter records by crime category
- View all crimes using the default All Crimes filter
- Dynamically rebuild the crime list when the selected category changes
- Scrollable crime record list
- Individual crime cards displaying:
  - crime category
  - approximate location
  - available outcome information
  - position within the filtered results
- Dynamic result numbering based on the selected category
- View Crimes data and filters reset correctly when performing a new search

### Categories Page

- Analyse the distribution of recorded crimes by category
- Dynamically calculate the number of records in each crime category
- Display human-readable crime category names
- Visualise crime category distribution using a horizontal bar chart
- Matplotlib chart embedded directly within the PyQt5 interface
- Display exact crime counts alongside individual bars
- Dynamically scale the chart based on the largest category
- Display reporting month and year
- Dynamically rebuild the chart when new search data is received
- Custom chart styling integrated with the application interface

### Interface

- Separate menu and results navigation
- Navigation between search and results interfaces
- New Search functionality
- Custom PyQt signals for communication between application components
- About page
- Custom QSS styling
- Dedicated styling for Overview, Categories, and View Crimes pages
- Modular application structure organised by feature

## Stage 4 — Results & Data Processing

### Stage 4a — Overview ✅

- Process raw Police API crime records
- Display searched postcode and geographic area
- Display reporting month and year
- Calculate and display total recorded crimes
- Determine and display the most common crime category
- Display the number of reports for the most common category
- Format API crime categories and dates for presentation
- Explain approximate and anonymised crime locations
- Add dedicated Overview styling

### Stage 4b — View Crimes ✅

- Display individual Police API crime records
- Allow users to filter records by crime category
- Provide an All Crimes view
- Display approximate crime locations
- Display available outcome information
- Handle records without outcome information
- Display individual records using reusable crime card widgets
- Number records according to the currently filtered results
- Display records inside a scrollable interface
- Dynamically clear and rebuild displayed records when filters change
- Reset crime filters and displayed records when a new search is performed
- Add dedicated View Crimes styling

### Stage 4c — Categories 🚧

- Calculate crime frequency by category
- Format API category names for presentation
- Visualise category distribution using a horizontal Matplotlib bar chart
- Embed Matplotlib directly within the PyQt5 results interface
- Display exact category counts alongside chart bars
- Dynamically scale the chart according to crime data
- Refresh the visualisation when a new search is performed
- Display reporting month and year
- Add dedicated Categories styling
- Improve category ordering for easier comparison

## Future Features

- Select crime data by year and month
- Analyse crime trends across multiple months
- Visualise historical crime trends
- Search history
- Revisit previous searches
- In-app usage guide
- Further UI refinement and testing

## Tech Stack

- Python
- PyQt5
- QSS
- REST APIs
- Requests
- Matplotlib

## Project Structure

```text
uk-crime-tracker/
├── main.py
│
├── app/
│   ├── __init__.py
│   ├── crime_tracker.py
│   │
│   ├── menu/
│   │   ├── __init__.py
│   │   ├── pages.py
│   │   └── widget.py
│   │
│   └── results/
│       ├── __init__.py
│       ├── pages.py
│       └── widget.py
│
├── api/
│   ├── __init__.py
│   ├── police.py
│   └── postcodes.py
│
├── styles/
│   ├── about.css
│   ├── base.css
│   ├── categories.css
│   ├── home.css
│   ├── navigation.css
│   ├── overview.css
│   ├── results.css
│   └── view_crimes.css
│
├── README.md
└── .gitignore
```