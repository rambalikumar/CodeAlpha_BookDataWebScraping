# Book Data Collection using Web Scraping

## 1. Problem Statement

Collecting book information manually from a website can take a lot of time.

This project uses web scraping to collect publicly available book information
from Books to Scrape and store it in a structured dataset.

---

## 2. Objectives

- Collect book information automatically
- Understand the HTML structure of a website
- Scrape data from multiple pages
- Extract book details from product pages
- Convert the collected data into a structured format
- Validate the collected dataset
- Save the final dataset as a CSV file

---

## 3. Website Used

**Books to Scrape**

Website: https://books.toscrape.com/

The website is designed for practicing web scraping.

---

## 4. Data Collected

The following information was collected:

- Book Title
- Price
- Rating
- Availability
- Category
- Product URL

Total records collected: **1000 books**

---

## 5. Future Analysis

The collected dataset can later be used for analysis such as:

- Category-wise book distribution
- Average price by category
- Rating distribution
- Price and rating relationship
- Most expensive books
- Highest-rated books

---

## 6. Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- Regular Expressions
- ThreadPoolExecutor
- Git
- GitHub

---

## 7. Scraping Approach

The project follows these steps:

1. Access the Books to Scrape website.
2. Navigate through 50 catalogue pages.
3. Extract book information from each page.
4. Clean and convert the price into a numerical value.
5. Convert the rating into a numerical value from 1 to 5.
6. Extract the URL of each book.
7. Visit individual book pages to collect the category.
8. Use controlled concurrency to collect categories.
9. Store the collected information in a Pandas DataFrame.
10. Validate the dataset.
11. Save the final dataset as a CSV file.

---

## 8. Data Validation

The final dataset was checked for:

- Missing values
- Data types
- Rating values
- Availability values
- Duplicate URLs
- Unknown categories
- Invalid prices
- Empty titles

Final validation results:

- Rows: **1000**
- Columns: **6**
- Missing values: **0**
- Duplicate URLs: **0**
- Unknown categories: **0**
- Invalid prices: **0**
- Empty titles: **0**

---

## 9. Project Files

```text
Task1_WebScraping/
│
├── scraper.py              -> Collect Data
├── validate_data.py        -> Verify Data
├── books_data.csv          -> Collected data
├── project_plan.md         -> Project documentation
└── requirements.txt        -> Required libraries

