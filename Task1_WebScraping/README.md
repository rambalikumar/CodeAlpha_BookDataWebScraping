# Book Data Collection using Web Scraping

## Overview

This project collects book information from the Books to Scrape website
using Python web scraping.

The collected data is cleaned, structured and saved as a CSV dataset
for further analysis.

## Objectives

- Collect book information automatically
- Scrape data from multiple pages
- Extract book categories from individual product pages
- Store the collected information in a structured dataset
- Validate the collected data

## Data Collected

The dataset contains:

- Title
- Price
- Rating
- Availability
- Category
- Product URL

Total records: **1000 books**

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- Regular Expressions
- ThreadPoolExecutor

## Project Structure

```text
Task1_WebScraping/
│
├── scraper.py
├── validate_data.py
├── books_data.csv
├── project_plan.md
├── requirements.txt
└── README.md