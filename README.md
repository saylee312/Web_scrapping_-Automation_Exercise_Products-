# Automation Exercise Job Scraper

## Overview
This project demonstrates how to extract structured data from a real-world website using Python web scraping techniques. The scraper collects the following details  by parsing HTML content.
- Product ID 
- Product Name  
- Category  
- Brand  
- Price  
- Availability  
- Product URL  
- Image URL
  
The project is designed for **learning and practice purposes**, focusing on understanding website structure and data extraction.

## Technologies used

- Python 3.x
- `requests` – for making HTTP requests
- `BeautifulSoup` (`bs4`) – for parsing HTML
- `pandas` – for data handling and CSV export
- `time` – to implement delays between requests

## Features

- Fetches data from a live website

- Parses HTML content efficiently

- Extracts relevant product details

- Handles missing or unavailable data

- Stores extracted data in a structured format

## Setup & Installation

### Create a Virtual Environment
bash
python -m venv venv

1. Activate the Virtual Environment
Windows: venv\Scripts\activate

macOS / Linux : source venv/bin/activate

2. Install Required Libraries
pip install requests beautifulsoup4

3. How to Run the Project
python file_name.py

# Output

The script extracts job listing data such as:

- Product ID 
- Product Name  
- Category  
- Brand  
- Price  
- Availability  
- Product URL  
- Image URL

The output can be printed to the console or saved for further analysis.

# Key Learnings

Understanding HTML and DOM structure

Web scraping using BeautifulSoup

Handling real-world website inconsistencies

Writing clean and readable Python code

# Disclaimer

This project is created for educational purposes only. Please review and respect the target website’s robots.txt and terms of service before scraping.

# Author
Saylee Bandal

