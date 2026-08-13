# UK Crime Tracker

A desktop application for exploring crime data across the UK by postcode.

## Status

🚧 Currently in development.

Stage 2 — the initial user interface and application structure — is complete.

Development is currently in Stage 3, focusing on API integration, results handling, and crime data retrieval. UK postcode lookup and validation have now been implemented.

## Current Features

- Desktop interface built with PyQt5
- Multi-page navigation
- UK postcode search interface
- Postcode lookup and validation using Postcodes.io
- Postcode location data retrieval
- API error and exception handling
- User-facing postcode error messages
- About page
- Custom QSS styling
- Modular stylesheet system
- Modular application and API package structure
- Separate application and menu widget layers

## Planned Features

- Results dashboard
- Retrieve local crime data using postcode coordinates
- Display crime statistics for the searched area
- Explore crime categories
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