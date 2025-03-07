# opensea-scrapers

## Description

This repository contains Python-based scrapers for OpenSea's NFT collection and product pages. These scrapers leverage the [Crawlbase Crawling API](https://crawlbase.com/crawling-api-avoid-captchas-blocks) to handle JavaScript rendering, CAPTCHA challenges, and anti-bot protections. The extracted data is processed using BeautifulSoup for HTML parsing and Pandas for structured storage.

➡ Read the full blog [here](https://crawlbase.com/blog/scrape-opensea-data-with-python/) to learn more.

## Scrapers Overview

### OpenSea Collection Page Scraper

The OpenSea Collection Page Scraper (`opensea_collection_scraper.py`) extracts:

- **NFT Title**
- **Price**
- **NFT Image URL**
- **Product Page Link**

It also handles pagination to ensure comprehensive data extraction. The extracted data is saved in a CSV file.

## OpenSea NFT Detail Page Scraper

The OpenSea NFT Detail Page Scraper (`opensea_nft_details_scraper.py`) extracts detailed NFT information, including:

- **NFT Tile**
- **Description**
- **Current Price**
- **Image URL**

The extracted data is saved in a CSV file.

## Environment Setup

Ensure that Python is installed on your system. Check the version using:

```bash
# Use python3 if required (for Linux/macOS)
python --version
```

Next, install the required dependencies:

```bash
pip install crawlbase beautifulsoup4 pandas
```

- **Crawlbase** – Handles JavaScript rendering and bypasses bot protections.
- **BeautifulSoup** – Parses and extracts structured data from HTML.
- **Pandas** – Stores and processes extracted data efficiently.

## Running the Scrapers

### Get Your Crawlbase Access Token

1. Sign up for Crawlbase [here](https://crawlbase.com/signup) to get an API token.
2. Use the JS token for OpenSea scraping, as OpenSea uses JavaScript-rendered content.

### Update the Scraper with Your Token

Replace "`CRAWLBASE_JS_TOKEN`" in the script with your Crawlbase JS Token.

### Run the Scraper

```bash
# For collection page scraping
python opensea_collection_scraper.py

# For NFT detail page scraping
python opensea_nft_details_scraper.py
```

The scraped data will be saved in `opensea_nft_collection_data.csv` or `'opensea_nft_data.csv`, depending on the script used.

## To-Do List

- Expand scrapers to extract additional NFT details like rarity score, sales history, and collection stats.
- Optimize data storage and add support for JSON and database integration.
- Improve scraper speed by implementing asynchronous requests.
- Integrate Crawlbase Smart Proxy to avoid rate limits and IP bans.
- Automate scheduled data extraction for real-time NFT tracking.

## Why Use This Scraper?

- ✔ Bypasses anti-bot protections with Crawlbase.
- ✔ Handles JavaScript-rendered content seamlessly.
- ✔ Extracts accurate and structured NFT data efficiently.
