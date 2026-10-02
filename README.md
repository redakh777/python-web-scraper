# Books to Scrape - Python Web Scraper

A robust Python web scraper that extracts book titles, prices, and star ratings from [Books to Scrape](http://books.toscrape.com/) and exports the clean data into a CSV file.

## Features
- **Pagination Handling**: Automatically iterates across multiple catalog pages.
- **Error & Exception Handling**: Uses `try/except` blocks to handle missing product attributes gracefully.
- **Anti-Blocking**: Configured with custom `User-Agent` headers to simulate legitimate browser requests.
- **CSV Data Export**: Cleans and outputs structured data using `pandas`.

## Tech Stack
- Python 3
- `requests`
- `BeautifulSoup4`
- `pandas`

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/redakh777/python-web-scraper.git](https://github.com/redakh777/python-web-scraper.git)
   cd python-web-scraper
