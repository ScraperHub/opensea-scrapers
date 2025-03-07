from crawlbase import CrawlingAPI
import pandas as pd
from bs4 import BeautifulSoup

# Initialize Crawlbase API with your access token
crawling_api = CrawlingAPI({'token': 'CRAWLBASE_JS_TOKEN'})

def make_crawlbase_request(url):
    options = {
        'ajax_wait': 'true',
        'scroll': 'true',
        'scroll_interval': '20'  # Scroll for 20 seconds
    }

    response = crawling_api.get(url, options)

    if response['headers']['pc_status'] == '200':
        html_content = response['body'].decode('utf-8')
        return html_content
    else:
        print(f"Failed to fetch the page. Crawlbase status code: {response['headers']['pc_status']}")
        return None

def scrape_opensea_collection(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    data = []

    # Find all NFT items in the collection
    nft_items = soup.select('div.Asset--loaded > article.AssetSearchList--asset')

    for item in nft_items:
        title = item.select_one('span[data-testid="ItemCardFooter-name"]').text.strip() if item.select_one('span[data-testid="ItemCardFooter-name"]') else ''
        price = item.select_one('div[data-testid="ItemCardPrice"] span[data-id="TextBody"]').text.strip() if item.select_one('div[data-testid="ItemCardPrice"] span[data-id="TextBody"]') else ''
        image = item.select_one('img')['src'] if item.select_one('img') else ''
        link = item.select_one('a.Asset--anchor')['href'] if item.select_one('a.Asset--anchor') else ''

        # Add the extracted data to the list
        data.append({
            'title': title,
            'price': price,
            'image_url': image,
            'link': f"https://opensea.io{link}"  # Construct the full URL
        })

    return data

def save_data_to_csv(data, filename='opensea_nft_collection_data.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    url = "https://opensea.io/collection/courtyard-nft"
    html_content = make_crawlbase_request(url)

    if html_content:
        data = scrape_opensea_collection(html_content)  # Extract data from HTML content
        save_data_to_csv(data)