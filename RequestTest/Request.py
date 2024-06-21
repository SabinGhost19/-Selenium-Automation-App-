import requests
from bs4 import BeautifulSoup

# Search URL
url = 'https://www.emag.ro/search/Laptop%20Gaming%20Lenovo%20IdeaPad%203%2015ACH6%20cu%20procesor%20AMD%20Ryzen%E2%84%A2%205%205500H%20pana%20la%204.20%20GHz,%2015.6"'

# Headers to mimic a browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send GET request
response = requests.get(url, headers=headers)
response.raise_for_status()

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all product prices
prices = soup.find_all('p', class_='product-new-price')

# Extract and print prices
for price in prices:
    price_text = price.get_text(strip=True).split(' ')[0]
    print(f'{price_text} Lei')
