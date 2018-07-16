from urllib.request import urlopen
from bs4 import BeautifulSoup

import re

site_links = []


def internal_links(linkURL):
    follow_html = urlopen('https://treehouse-projects.github.io/horse-land/{}'
                          .format(linkURL))
    soup = BeautifulSoup(follow_html, 'html.parser')
    return soup.find('a', href=re.compile('(.html)$'))


def external_links(linkURL):
    follow_html = urlopen('https://{}'.format(linkURL))
    soup = BeautifulSoup(follow_html, 'html.parser')
    return soup.find('a', href=re.compile('^.(https)'))


if __name__ == '__main__':
    urls = external_links('treehouse-projects.github.io/horse-land/index.html')
    while len(urls) > 0:
        page = urls.attrs['href']
        if page not in site_links:
            site_links.append(page)
            print(page)
            print('\n===================================\n')
            urls = external_links(page)
        else:
            break
