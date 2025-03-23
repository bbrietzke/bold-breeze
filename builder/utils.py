from urllib.request import urlopen
from bs4 import BeautifulSoup

def beautify_the_soup(url):
    return BeautifulSoup(urlopen(url).read().decode("utf-8"), 'html.parser')