# UK Crime Tracker

A desktop application for exploring crime data across the UK by postcode.

## Status

🚧 Currently in development.

Stage 2 — the initial user interface and application structure — is complete.

Development is currently in Stage 3. Postcode API integration and the results interface are now implemented. Development is moving into Police API integration to retrieve real crime data using postcode coordinates.

## Current Features

- Desktop interface built with PyQt5
- Multi-page application navigation
- UK postcode search interface
- Postcode lookup and validation using Postcodes.io
- Postcode location and coordinate retrieval
- API error and exception handling
- User-facing postcode error messages
- Results interface with separate navigation
- Overview and Categories result pages
- Navigation between search and results interfaces
- Custom PyQt signals for communication between application components
- New Search functionality
- About page
- Custom QSS styling
- Modular stylesheet system
- Modular application and API package structure

## Planned Features

- Retrieve local crime data using postcode coordinates
- Process and organise Police API responses
- Display crime statistics in the results overview
- Explore crime data by category
- Visualise crime data with charts and trends
- Search history
- Revisit previous searches
- In-app usage guide

## Tech Stack

- Python
- PyQt5
- QSS
- REST APIs
- Requests

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
│   └── postcodes.py
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