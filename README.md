<h3 style="text-align:center;font-weight: 300;" align="center">
  <img src="/img/logo.png" width="400px">
</h3>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg?style=flat-square">
  <img src="https://img.shields.io/badge/downloads-0k-yellow.svg?style=flat-square">
  <img src="https://img.shields.io/badge/build-passing-yellow.svg?style=flat-square">
</p>


> Micheal, the Aspiring Consultant/PM guy asked me to check out his blog site, well let's use it to learn some web-scraping.




<!-- ## Features -->

## External Libraries

Third Party libraries are used in this project

Package    |      Description
---------- | :--------------------:
`bs4`  | Beautiful Soup
`requests`  | Source requesting
`csv`  |  Export CSV files


## Code

a Hello World project for web scraping, no explanation

```python
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
```


## Demo

`bash` version:
![bash](/img/bash.png)

`csv` version:
![csv](/img/csv.png)


## License

🌱 MIT 🌱


[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fyuzhoujr%2Fcs_progression.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fyuzhoujr%2Fcs_progression?ref=badge_large)

---

> ![home](http://yuzhoujr.com/emoji/home.svg)
[yuzhoujr.com](http://www.yuzhoujr.com) &nbsp;&middot;&nbsp;
> ![github](http://yuzhoujr.com/emoji/github.svg)  [@yuzhoujr](https://github.com/yuzhoujr) &nbsp;&middot;&nbsp;
> ![linkedin](http://yuzhoujr.com/emoji/linkedin.svg)  [@yuzhoujr](https://linkedin.com/in/yuzhoujr)
