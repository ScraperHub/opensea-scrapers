from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import pandas as pd

# Initialize Crawlbase API with your access token
crawling_api = CrawlingAPI({'token': 'CRAWLBASE_JS_TOKEN'})

def make_crawlbase_request(url):
    options = {
        'ajax_wait': 'true',
        'page_wait': '5000'
    }

    response = crawling_api.get(url, options)

    if response['headers']['pc_status'] == '200':
        html_content = response['body'].decode('utf-8')
        return html_content
    else:
        print(f"Failed to fetch the NFT detail page. Crawlbase status code: {response['headers']['pc_status']}")
        return None

def scrape_opensea_nft_detail(html_content, url):
    soup = BeautifulSoup(html_content, 'html.parser')

    title = soup.select_one('h1.item--title').text.strip() if soup.select_one('h1.item--title') else ''
    description = soup.select_one('div.item--description').text.strip() if soup.select_one('div.item--description') else ''
    price = soup.select_one('div.Price--amount').text.strip() if soup.select_one('div.Price--amount') else ''
    image_urls = [img['src'] for img in soup.select('div.media-container img')]
    link = url  # The link is the current URL

    nft_data = {
        'title': title,
        'description': description,
        'price': price,
        'images_url': image_urls,
        'link': link
    }

    return nft_data

def save_nft_data_to_csv(data, filename='opensea_nft_data.csv'):
    df = pd.DataFrame([data])  # Convert the single NFT data dictionary to a DataFrame
    df.to_csv(filename, index=False)
    print(f"NFT data saved to {filename}")

# Example usage
if __name__ == "__main__":
    nft_url = "https://opensea.io/assets/matic/0x251be3a17af4892035c37ebf5890f4a4d889dcad/94953658332979117398233379364809351909803379308836092246404100025584049123386"
    html_content = make_crawlbase_request(nft_url)

    if html_content:
        nft_data = scrape_opensea_nft_detail(html_content, nft_url)  # Extract data from HTML content
        save_nft_data_to_csv(nft_data)  # Save NFT data to CSV