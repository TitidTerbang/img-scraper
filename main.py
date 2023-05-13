from bs4 import BeautifulSoup
import requests

website = 'https://nsfwx.pics/4650.html'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# image = soup.img['src']
images = soup.find_all('img')
# print(images)

imagesrc = []
for image in images:
    imagesrc.append(image['src'])
print(imagesrc)

for image in imagesrc:
    webs = requests.get(image)
    filename = 'bro/' + image.split('/')[-1]
    open(filename, 'wb').write(webs.content)

# for image in images:
#     webs = requests.get(image)
#     open('images/' + image.split('/')[-1], 'wb').write(webs.content)
# box = soup.find('article', class_= 'main-article')

# title = soup.find('h1').get_text()
# transcript = box.find('div', class_= 'full-script').get_text(strip=True, separator='\n')
# print(title)
# print(transcript)