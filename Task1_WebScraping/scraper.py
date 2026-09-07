from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import pandas as pd
from pathlib import Path



def get_category(book_url):
    for attempt in range(3):
        try:
            response = requests.get(book_url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            breadcrumb = soup.find("ul", class_="breadcrumb")

            if breadcrumb is None:
                return "Unknown"
        
            items = breadcrumb.find_all("li")

            if len(items) < 3:
                return "Unknown"

            return items[2].get_text(strip=True)


        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {book_url} - > {e}")

    return "Unknown"



books_in_store = []

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


for page in range(1, 51):

    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

    except requests.RequestException as e:
        print(f"Page {page} failed: {e}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.find("h3").find("a")

        raw_price = book.find("p", class_="price_color")
        price_text = raw_price.get_text(strip=True)
        clean_price = float(re.sub(r"[^0-9.]", "", price_text))

        rating = book.find("p", class_="star-rating")
        rating_class = rating.get("class")
        clean_rating = rating_map[rating_class[1]]

        availability = book.find("p", class_="instock availability")

        full_url = urljoin(url, title.get("href"))

        book_data = {
            "title": title.get("title"),
            "price": clean_price,
            "rating": clean_rating,
            "availability": availability.get_text(strip=True),
            "url": full_url
        }

        books_in_store.append(book_data)


df = pd.DataFrame(books_in_store)


book_urls = df["url"].tolist()

categories = []
with ThreadPoolExecutor(max_workers=5) as executor:

    for i, category in enumerate(executor.map(get_category, book_urls), start=1):

        categories.append(category)

        if i % 100 == 0:
            print(f"Fetching categories: {i}/{len(book_urls)}")


df["category"] = categories


# Save dataset

output_file = Path(__file__).resolve().parent / "books_data.csv"

df.to_csv(output_file, index=False)

print(f"Dataset saved to: {output_file}")
print(f"Dataset shape: {df.shape}")
