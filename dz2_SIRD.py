import requests
from bs4 import BeautifulSoup
import urllib.parse
import json
from datetime import datetime, time, timedelta
import time
import re
from fake_useragent import UserAgent


all_book_data = []

for i in range(1, 4):
    url = f'http://books.toscrape.com/catalogue/page-{i}.html'
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})
    if response.status_code == 200:
       soup = BeautifulSoup(response.content, 'html.parser')
       book_links = [a['href'] for a in soup.select('article.product_pod h3 a')]

       for link in book_links:
          book_url = urllib.parse.urljoin('http://books.toscrape.com/catalogue/', link)
          book_response = requests.get(book_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})

          if book_response.status_code == 200:
           book_soup = BeautifulSoup(book_response.content, 'html.parser')
           book_data = {}
           book_data['title'] = book_soup.h1.text
           book_data['price'] = book_soup.find('p', class_='price_color').text
           book_data['availability'] = book_soup.find('p', class_='instock availability').text.strip()


    else:
     print(f"Failed to retrieve book details from {book_url}")
         
     print(f"Failed to retrieve page {url}")  

all_book_data.append(book_data)
time.sleep(1)


with open('book_data.json', 'w') as f:
 json.dump(all_book_data, f, indent = 4)

print("Data saved to book_data.json")

