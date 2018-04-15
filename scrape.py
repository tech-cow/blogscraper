from bs4 import BeautifulSoup
import requests
import csv

src = requests.get('https://floating-crag-22061.herokuapp.com/blogs').text
soup = BeautifulSoup(src, 'lxml')

csv_file = open('blog_content.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Date', 'Summary', 'Blog Link'])

content_container = soup.find('div', class_= "twelve wide computer twelve wide tablet column main text")
for article in content_container.find_all('div', class_='item'):
    content = article.find('div', class_='content')
    content_headline = content.find('a', class_='header').text
    content_date = content.find('div', class_='meta').span.text
    content_summary = content.find('div', class_='description').p.text
    content_readmore = 'https://floating-crag-22061.herokuapp.com' + article.find('a', class_="ui medium image fluid image-fixed")['href']
    csv_writer.writerow([content_headline, content_date, content_summary, content_readmore])
csv_file.close()
