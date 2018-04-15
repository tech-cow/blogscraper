from bs4 import BeautifulSoup
import requests

with open('blog.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

content = {
        'quote' : '',
        'introduction' : '',
        'p.s.?' : ''
}

content_container = soup.find('div', class_= "twelve wide computer twelve wide tablet column main text")
# article = content_container.find('div', class_='item')

counter = 1
print('\n')
print('\n')

for article in content_container.find_all('div', class_='item'):
    content = article.find('div', class_='content')

    content_title = content.find('a', class_='header').text
    content_date = content.find('div', class_='meta').span.text
    content_description = content.find('div', class_='description').p.text

    print('----------Article ' + str(counter) + '----------')
    print(content_title)
    print(content_date)
    print(content_description)
    print('\n')
    counter += 1

# readmore_link = article.find('a', class_="ui medium image fluid image-fixed")['href']
# print(readmore_link)
