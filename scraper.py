import requests
from bs4 import BeautifulSoup

def scrape(url):
    r = requests.get(url)
    print(f'Status: {r.status_code}')

if __name__ == '__main__':
    scrape('https://example.com')
