# UK Crime Tracker

A desktop application for exploring crime data across the UK by postcode.

## Status

🚧 Currently in development.

The initial user interface is complete. Development is now moving into API integration and crime data retrieval.

## Current Features

- Desktop interface built with PyQt5
- Multi-page navigation
- UK postcode search interface
- About page
- Custom QSS styling
- Modular stylesheet system

## Planned Features

- Validate and search UK postcodes
- Retrieve local crime data from public APIs
- Display crime statistics for the searched area
- Explore crime categories
- Visualise crime data with charts and trends
- View previous searches
- Results dashboard
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
├── pages.py
├── styles/
│   ├── ...
│   ├── home.css
│   └── about.css
└── README.md