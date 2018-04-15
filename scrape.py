from bs4 import BeautifulSoup
import requests

with open('blog.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())

title = soup.title.text

item = soup.find('div', class_='item')
print(item.prettify())
