from bs4 import BeautifulSoup
import requests

# website = 'https://imagehaha.com/1j0dlmxpfuyx/1228209.jpg.html'
website = 'https://nsfwx.pics/4650.html'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# image = soup.img['src']
images = soup.find_all('a')
# print(images)

imagesrc = []
for image in images:
    imagesrc.append(image['href'])
# print(imagesrc)

filterimg = [filt for filt in imagesrc if 'https://imagehaha.com/' in filt]
print(filterimg)
# for image in imagesrc:
#     webs = requests.get(image)
#     filename = 'bro/' + image.split('/')[-1]
#     open(filename, 'wb').write(webs.content)

# for image in images:
#     webs = requests.get(image)
#     open('images/' + image.split('/')[-1], 'wb').write(webs.content)
# box = soup.find('article', class_= 'main-article')

# title = soup.find('h1').get_text()
# transcript = box.find('div', class_= 'full-script').get_text(strip=True, separator='\n')
# print(title)
# print(transcript)