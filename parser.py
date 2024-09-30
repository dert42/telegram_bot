from bs4 import BeautifulSoup
import requests

from config import url


def parse():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    usd = soup.find('span', class_='chart__info__sum')
    return usd.text
