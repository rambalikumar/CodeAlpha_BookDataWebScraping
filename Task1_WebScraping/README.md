# Book Data Collection using Web Scraping

A Python-based web scraping project that collects publicly available book information from the Books to Scrape website and stores it in a structured CSV dataset.

## Overview

This project uses Python to scrape book information from multiple catalogue pages of the Books to Scrape website.

The scraper collects basic book information and also visits individual product pages to extract the book category.

The final dataset contains **1,000 book records** with **6 attributes**.

## Objectives

- Collect book information automatically
- Scrape data from multiple pages
- Extract book categories from individual product pages
- Clean and structure the collected data
- Validate the collected dataset
- Save the final dataset as a CSV file

## Data Collected

| Field | Description |
|---|---|
| Title | Name of the book |
| Price | Price of the book |
| Rating | Rating from 1 to 5 |
| Availability | Stock availability |
| Category | Book category |
| URL | Product page URL |

**Total records: 1,000 books**

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- Regular Expressions
- ThreadPoolExecutor
- Git & GitHub

## Project Structure

```text
Task1_WebScraping/
|
|-- scraper.py
|-- validate_data.py
|-- books_data.csv
|-- project_plan.md
|-- requirements.txt
`-- README.md