from bs4 import BeautifulSoup
import requests

with open('blog.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

content = {
        'quote' : '',
        'introduction' : '',
        'p.s.?' : ''
}

content = soup.find('div', class_= "twelve wide computer twelve wide tablet column main text")
article = content.find('div', class_='item')

img_source = article.
