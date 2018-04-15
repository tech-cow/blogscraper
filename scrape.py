from bs4 import BeautifulSoup
import requests

with open('blog.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

content = {
        'Quote' : '',
        'Introduction' : '',
        'p.s.?' : ''
}

for key, val in content.items():
    print(key + ':' + val)
