import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.youtube.com/feed/subscriptions"
try:
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    try:
        for link in soup.find_all('a'):
            if "h" in link.get('href'):
                print(link.get('href'))
        open("pages.txt", "w").write(soup.prettify())
    except:
        print("cannot save in file")
except:
    print("cannot open page")