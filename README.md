# UK Crime Tracker

A desktop application for exploring and understanding local crime data across the UK by postcode.

## Status

🚧 Currently in development.

Stage 3 — API integration and crime data retrieval — is complete.

Development is now moving into Stage 4: data processing and results presentation. The application can validate a UK postcode, retrieve its geographic coordinates, use those coordinates to retrieve street-level crime records, and pass both datasets into the results interface.

Stage 4 will focus on transforming the raw crime records into useful statistics, visualisations, and searchable crime information.

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
- Results interface with separate navigation
- Overview and Categories result pages
- Navigation between search and results interfaces
- Custom PyQt signals for communication between application components
- New Search functionality
- About page
- Custom QSS styling
- Modular stylesheet system
- Modular application and API package structure

## Stage 4 — Results & Data Processing

Planned work for the current development stage:

- Process and aggregate raw Police API crime records
- **Overview** — display postcode, area, reporting month, total recorded crimes, and headline statistics
- **Categories** — analyse crime types and visualise their distribution using a Matplotlib bar chart
- **View Crimes** — allow users to select a crime category and explore individual crime records
- Display approximate crime locations and available outcome information
- Add results-specific styling and presentation

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
- Matplotlib *(planned for Stage 4)*

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
│   └── about.css
│
├── README.md
└── .gitignore
```