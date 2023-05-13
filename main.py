from bs4 import BeautifulSoup
import requests

# the website
website = 'https://nsfwx.pics/4650.html'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
images = soup.find_all('a')

imagesrc = []
for image in images:
    imagesrc.append(image['href'])

#filter the source
filterimg = [filt for filt in imagesrc if 'https://imagehaha.com/' in filt]
filterimg_str = '\n'.join(filterimg)
linetunnel = filterimg_str.split()

for image in linetunnel:
    site = requests.get(image)
    cont = site.text
    soups = BeautifulSoup(cont, 'lxml')
    tunnelimage = soups.img['src']

    webs = requests.get(tunnelimage)
    filename = 'bro/' + tunnelimage.split('/')[-1]
    open(filename, 'wb').write(webs.content)