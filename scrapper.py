import os
import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/23283045/importerror-no-module-named-requests-python-3-4-0'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
if os.path.isfile('test'):
    os.remove('test')
file = open("test", 'wb')
links = soup.find_all('a')


for link in links:
        href = str(link.get('href')) + '\n'
        file.write(href.encode())
file.close()
