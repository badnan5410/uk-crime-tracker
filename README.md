# UK Crime Tracker

A desktop application for exploring and understanding local crime data across the UK by postcode.

## Status

🚧 Currently in development.

Stages 1–5 are complete, covering the application foundation, postcode search, API integration, crime data processing, the core results interface, and reporting date selection.

The application can now retrieve street-level crime data for a UK postcode and a selected reporting month and year, and present it across three results pages:

- **Overview** — summary statistics and location information
- **Categories** — crime category distribution visualised with Matplotlib
- **View Crimes** — individual crime records with category filtering

The next planned step is **Stage 6: Search History**, which will allow users to store and revisit previous searches.

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
- Geographic and crime data passed between application components
- Dynamic results refresh when new search data is received

### Date Selection

- Separate year and month selectors on the search page
- Year options generated dynamically from the current year back to 2023
- Month options refreshed when the selected year changes
- July–December offered for 2023; all twelve months offered for intervening years
- Current-year options limited to months before the current month
- Month selector shown after a year is chosen
- Placeholder options disabled after a valid selection
- Validation requiring a postcode, year, and month before making API requests
- Selected date formatted as `YYYY-MM` and passed into Police API requests
- Reporting month and year displayed with the results
- A message showing the selected reporting period when the API returns no crime records
- Postcode, error message, and date selectors reset when starting a new search

The date selectors use calendar-based limits rather than checking the Police API's published reporting periods. A selectable month may not yet have published data.

### Crime Data Processing

- Crime record processing and aggregation
- Total recorded crime calculation
- Most common crime category calculation
- Crime category frequency calculation
- Crime categories ordered by frequency for easier comparison
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

### Categories Page

- Analyse the distribution of recorded crimes by category
- Dynamically calculate the number of records in each crime category
- Display categories ordered from highest to lowest crime count
- Display human-readable crime category names
- Visualise crime category distribution using a horizontal bar chart
- Matplotlib chart embedded directly within the PyQt5 interface
- Display exact crime counts alongside individual bars
- Dynamically scale the chart based on the largest category
- Display reporting month and year
- Dynamically rebuild the chart when new search data is received
- Custom chart styling integrated with the application interface

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

### Interface

- Separate menu and results navigation
- Navigation between search and results interfaces
- New Search functionality
- Custom PyQt signals for communication between application components
- About page
- Custom QSS styling
- Stylesheets organised by application area
- Shared global and navigation styling
- Dedicated styling for menu and results pages
- Modular application structure organised by feature

## Development Roadmap

### Stage 1 — Application Foundation ✅

- Create the main PyQt5 application
- Build menu and results interfaces
- Implement multi-page navigation
- Establish modular project structure
- Add custom QSS styling

### Stage 2 — Search & Postcode Handling ✅

- Add postcode search interface
- Validate user postcode input
- Retrieve postcode location information
- Handle invalid postcode searches
- Display user-facing validation messages

### Stage 3 — API Integration ✅

- Integrate Postcodes.io
- Retrieve latitude and longitude from postcode searches
- Integrate the UK Police Data API
- Retrieve street-level crime records
- Implement API error and exception handling
- Pass retrieved data into the results interface

### Stage 4 — Results & Data Processing ✅

#### Stage 4a — Overview ✅

- Process raw Police API crime records
- Display searched postcode and geographic area
- Display reporting month and year
- Calculate and display total recorded crimes
- Determine and display the most common crime category
- Display the number of reports for the most common category
- Format API crime categories and dates for presentation
- Explain approximate and anonymised crime locations
- Add dedicated Overview styling

#### Stage 4b — View Crimes ✅

- Display individual Police API crime records
- Allow users to filter records by crime category
- Provide an All Crimes view
- Display approximate crime locations
- Display available outcome information
- Handle records without outcome information
- Display individual records using reusable crime card widgets
- Number records according to the selected category
- Display records inside a scrollable interface
- Dynamically clear and rebuild displayed records when filters change
- Reset crime filters and displayed records when a new search is performed
- Add dedicated View Crimes styling

#### Stage 4c — Categories ✅

- Calculate crime frequency by category
- Format API category names for presentation
- Order categories by crime frequency
- Visualise category distribution using a horizontal Matplotlib bar chart
- Embed Matplotlib directly within the PyQt5 results interface
- Display exact crime counts alongside chart bars
- Dynamically scale the chart according to crime data
- Refresh the visualisation when a new search is performed
- Display reporting month and year
- Add dedicated Categories styling

### Stage 5 — Date Selection ✅

- Allow users to select a crime reporting month
- Allow users to select a crime reporting year
- Populate year options dynamically and refresh month options when the year changes
- Apply date limits and validate selections before searching
- Pass the selected date into Police API requests
- Display results for the selected reporting period
- Show a reporting-period message when no crime records are returned
- Reset date selectors when starting a new search

### Stage 6 — Search History (Next)

- Store previous searches
- Display previous postcode searches
- Allow users to revisit previous searches

### Stage 7 — How To Use

- Add an in-app usage guide
- Explain postcode searching and results
- Explain the Overview, Categories, and View Crimes pages

### Stage 8 — Testing, UI Polish & v1

- Improve defensive handling of API data
- Test search and navigation flows
- Test results across different postcodes and crime volumes
- Refine UI consistency
- Improve error handling where necessary
- Final code and project structure cleanup
- Prepare the first portfolio-ready release

## Future Features

- Analyse crime trends across multiple months
- Visualise historical crime trends
- Expanded historical data exploration
- Further performance improvements for large result sets

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
├── api/
│   ├── __init__.py
│   ├── police.py
│   └── postcodes.py
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
├── styles/
│   ├── global/
│   │   ├── base.css
│   │   └── navigation.css
│   │
│   ├── menu/
│   │   ├── about.css
│   │   └── home.css
│   │
│   └── results/
│       ├── categories.css
│       ├── overview.css
│       └── view_crimes.css
│
├── README.md
└── .gitignore
```