import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/', timeout=10)

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify())
