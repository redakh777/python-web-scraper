import csv
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Target URL
BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

# Request headers to emulate standard browser:
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

all_books = []

print("Starting scraper...")

# 2. Handle Pagination (Scrape pages 1 through 3)
for page_num in range(1, 4):
    url = BASE_URL.format(page_num)
    print(f"Scraping page {page_num}: {url}")

    # Send a GET request to fetch page HTML
    response = requests.get(url, headers=HEADERS)

    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to load page {page_num}")
        continue

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book containers on the page
    books = soup.find_all("article", class_="product_pod")

    # 3. Extract Data & Add Error Handling
    for book in books:
        # Title
        try:
            title = book.h3.a["title"]
        except (AttributeError, KeyError):
            title = "N/A"

        # Price
        try:
            price = book.find("p", class_="price_color").text.strip()
        except AttributeError:
            price = "N/A"

        # Rating
        try:
            # Rating class is stored like: ["star-rating", "Three"]
            rating_classes = book.find("p", class_="star-rating")["class"]
            rating = (
                rating_classes[1] if len(rating_classes) > 1 else "Unrated"
            )
        except (AttributeError, KeyError):
            rating = "Unrated"

        # Store in list as a dictionary
        all_books.append({"Title": title, "Price": price, "Rating": rating})

    # Politeness delay to avoid overloading server
    time.sleep(1)

# 4. Export to CSV using pandas
df = pd.DataFrame(all_books)
df.to_csv("books_scraped.csv", index=False)

print(f"\nDone! Scraped {len(all_books)} books across 3 pages.")
print("Saved to 'books_scraped.csv'.")