# UK Crime Tracker

A desktop application for exploring and understanding local crime data across the UK by postcode.

## Status

🚧 Currently in development.

Stage 3 — API integration and crime data retrieval — is complete.

Development is currently in Stage 4: data processing and results presentation.

Stage 4a — the Overview page — is complete. Raw Police API crime records are now processed into useful summary information, including total recorded crimes, the most common crime category, location information, and reporting period.

Development is moving into Stage 4b, which will focus on allowing users to explore individual crime records by category.

## Current Features

- Desktop interface built with PyQt5
- Multi-page application navigation
- UK postcode search interface
- Postcode lookup and validation using Postcodes.io
- Postcode location and coordinate retrieval
- Street-level crime data retrieval using the UK Police Data API
- Crime searches based on postcode latitude and longitude
- Two-stage API search and validation flow
- API error and exception handling
- User-facing API error messages
- Geographic and crime data passed into the results interface
- Dynamic results refresh when new search data is received
- Crime record processing and aggregation
- Total recorded crime calculation
- Most common crime category calculation
- Police API reporting date formatting
- Dynamic Overview page displaying postcode, area, reporting month, and crime statistics
- Results interface with separate navigation
- Overview and Categories result pages
- Navigation between search and results interfaces
- Custom PyQt signals for communication between application components
- New Search functionality
- About page
- Custom QSS styling
- Results-specific Overview styling
- Modular stylesheet system
- Modular application and API package structure

## Stage 4 — Results & Data Processing

### Stage 4a — Overview ✅

- Process raw Police API crime records
- Display searched postcode and geographic area
- Display reporting month and year
- Calculate and display total recorded crimes
- Determine and display the most common crime category
- Display the number of reports for the most common category
- Format API crime categories and dates for presentation
- Provide context about approximate and anonymised crime locations
- Custom Overview page styling

### Stage 4b — View Crimes 🚧

- Allow users to select a crime category
- Explore individual crime records within the selected category
- Display approximate crime locations
- Display available outcome information

### Stage 4c — Categories

- Analyse the distribution of crime categories
- Visualise crime categories using a Matplotlib bar chart
- Integrate Matplotlib visualisations into the PyQt5 results interface

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
- Matplotlib *(planned for Stage 4c)*

## Project Structure

```text
uk-crime-tracker/
├── main.py
│
├── app/
│   ├── __init__.py
│   ├── crime_tracker.py
│   ├── menu_widget.py
│   ├── results_widget.py
│   └── pages.py
│
├── api/
│   ├── __init__.py
│   ├── postcodes.py
│   └── police.py
│
├── styles/
│   ├── base.css
│   ├── navigation.css
│   ├── home.css
│   ├── about.css
│   └── overview.css
│
├── README.md
└── .gitignore