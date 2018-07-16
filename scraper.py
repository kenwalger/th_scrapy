from urllib.request import urlopen
from bs4 import BeautifulSoup

import re

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')

# print(soup)

# print(soup.prettify())

# print(soup.title)
#
# print(soup.div)
#
# divs = soup.findAll('div', {'class': 'featured'})
# for div in divs:
#     print(div)

# divs = soup.find('div', {'class': 'featured'})
# print(divs)

featured_header = soup.find('div', {'class': 'featured'})
print(featured_header.get_text())

for button in soup.find_all(class_='button button--secondary'):
    print(button)

for link in soup.find_all('a'):
    print(link.get('href'))

print('\n=================\n')

for link in soup.find_all('a', href=re.compile('^(https)')):
    if 'href' in link.attrs:
        print(link.attrs['href'])

print('\n=================\n')

for link in soup.find_all('a', href=re.compile('(.html)$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])

