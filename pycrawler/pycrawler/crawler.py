import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pycrawler.models import Link,Session
base_url='https://www.sqlalchemy.org'
def crawl(url,depth,current_depth=0):
    urls = []
    l =Link(url=url,state='started',depth=1)
    s = Session()
    s.add(l)
    s.commit()
    with urllib.request.urlopen(url) as response:
        html = response.read()
        soup = BeautifulSoup(html,'html.parser')
        for i,a in enumerate(soup.find_all('a')):
            if not a.has_attr('href'):
                continue
            href = a['href']
            href=urljoin(url, href)
            if not href.startswith(base_url):
                continue
            print(href)
            l =Link(url=href,state='pending',depth=1)
            s = Session()
            s.add(l)
            s.commit()
            