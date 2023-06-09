from bs4 import BeautifulSoup
import requests

# the website
website = ''
result = requests.get(website)

if result.status_code == 200:
    content = result.text

    soup = BeautifulSoup(content, 'lxml')
    images = soup.find_all('a')

    imagesrc = []
    for image in images:
        imagesrc.append(image['href'])
    # filter the source and get the higher image
    filterimg = [filt for filt in imagesrc if 'https://images-na.ssl' in filt]
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

else:
    print('Error')
