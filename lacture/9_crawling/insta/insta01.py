from bs4 import BeautifulSoup
import requests

tag = input('search tags: ')
url = f'https://www.instagram.com/explore/tags/{tag}'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)

pic = soup.select('.KL4Bh>img')
print(pic)
