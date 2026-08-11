# UK Crime Tracker

A desktop application for exploring crime data across the UK by postcode.

## Status

🚧 Currently in development.

Stage 2 — the initial user interface and application structure — is complete. Development is now moving into Stage 3: API integration and crime data retrieval.

## Current Features

- Desktop interface built with PyQt5
- Multi-page navigation
- UK postcode search interface
- About page
- Custom QSS styling
- Modular stylesheet system
- Organised application package structure

## Planned Features

- Validate and search UK postcodes
- Retrieve local crime data from public APIs
- Display crime statistics for the searched area
- Explore crime categories
- Visualise crime data with charts and trends
- Results dashboard
- Search history
- Revisit previous searches
- In-app usage guide

## Tech Stack

- Python
- PyQt5
- QSS
- REST APIs *(integration upcoming)*

## Project Structure

```text
uk-crime-tracker/
├── main.py
│
├── app/
│   ├── __init__.py
│   ├── app.py
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