# UK Crime Tracker

A Python desktop application for exploring local crime data by postcode and reporting month.

Search for a postcode, choose a month and year, and explore the results through summary statistics, a category chart, and filterable crime records.

## Status

✅ Core application complete.

This version includes postcode search, API integration, reporting date selection, and three results pages:

- **Overview** — summary statistics and location information
- **Categories** — crime category distribution visualised with Matplotlib
- **View Crimes** — individual crime records with category filtering

Development concluded after Stage 5. Search History and the in-app How To Use page are outside the scope of this version.

## Features

### 🔎 Postcode Search

- Postcode input validation
- Location and coordinate retrieval using Postcodes.io
- Street-level crime data retrieval using the UK Police Data API
- Searches based on the postcode’s latitude and longitude
- User-facing validation and API error messages
- Results refreshed for each successful search

### 📅 Reporting Date Selection

- Separate year and month selectors
- Year options generated dynamically from the current year back to 2023
- Month options refreshed when the selected year changes
- July–December offered for 2023; all twelve months offered for intervening years
- Current-year options limited to months before the current month
- Validation requiring a postcode, year, and month before searching
- Selected reporting date passed to the Police API as `YYYY-MM`
- Reporting month and year displayed throughout the results
- A message identifying the selected reporting period when no records are returned
- Search fields and error messages reset when starting a new search

### 📊 Overview

- Searched postcode, district, and region
- Reporting month and year
- Total recorded crimes returned by the search
- Most common crime category and its record count
- Information explaining approximate and anonymised crime locations

### 📈 Categories

- Crime records grouped and counted by category
- Categories ordered from highest to lowest count
- Human-readable category names
- Horizontal Matplotlib bar chart embedded within the interface
- Exact counts displayed alongside chart bars
- Chart refreshed for each successful search

### 📋 View Crimes

- Scrollable list of individual crime cards
- Category filtering, including an All Crimes option
- Cards displaying:
  - Crime category
  - Approximate location
  - Available outcome information
  - Position within the filtered results
- Records without outcome information displayed as “Unresolved”
- List and numbering updated when the filter changes
- Filters reset for a new search

### 🖥️ Interface and Structure

- Desktop interface built with PyQt5
- Separate menu and results navigation
- About page and New Search functionality
- Custom PyQt signals for communication between components
- QSS stylesheets organised by application area
- Modular separation of interface, API access, and data-processing responsibilities

## Using the Application

1. Open the application and enter a postcode on the Home page.
2. Select a reporting year, then a month.
3. Submit the search.
4. Explore the **Overview**, **Categories**, and **View Crimes** pages.
5. Use **New Search** to return to the search form.

An internet connection is required to retrieve postcode and crime data.

## Data Notes and Limitations

- Date options use calendar-based limits rather than the Police API’s published reporting periods. A selectable month may not have available data.
- Crime locations are approximate and anonymised.
- Results reflect the records returned by the API for the search location and reporting period.
- Data availability depends on the external services and their geographic and reporting coverage.
- “Unresolved” is the application’s fallback label when outcome information is missing; it does not establish the current status of an investigation.
- Search history is not stored in this version.

## Development Milestones

### Stage 1 — Application Foundation ✅

- Created the PyQt5 application
- Built menu and results interfaces
- Implemented multi-page navigation
- Established the modular project structure and QSS styling

### Stage 2 — Search and Postcode Handling ✅

- Added postcode input and validation
- Retrieved postcode location information
- Displayed user-facing validation messages

### Stage 3 — API Integration ✅

- Integrated Postcodes.io and the UK Police Data API
- Used postcode coordinates to retrieve street-level crime records
- Added API error and exception handling
- Passed retrieved data into the results interface

### Stage 4 — Results and Data Processing ✅

- Built the Overview, Categories, and View Crimes pages
- Calculated totals and category frequencies
- Embedded a Matplotlib category chart
- Added reusable crime cards and category filtering
- Implemented results refresh and dedicated page styling

### Stage 5 — Date Selection ✅

- Added dynamic reporting year and month selectors
- Validated selections before searching
- Passed the selected date into API requests
- Displayed the reporting period across results
- Added handling for searches returning no records
- Reset date selections when starting a new search

## Tech Stack

- **Python** — application logic
- **PyQt5** — desktop interface
- **QSS** — interface styling
- **Requests** — HTTP requests to REST APIs
- **Matplotlib** — crime category visualisation
- **Git and GitHub** — version control

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