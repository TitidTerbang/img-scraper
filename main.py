from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/American_Psycho-144084'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', class_= 'main-article')

title = soup.find('h1').get_text()
transcript = box.find('div', class_= 'full-script').get_text(strip=True, separator='\n')
print(title)
print(transcript)