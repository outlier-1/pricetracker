import requests
from bs4 import BeautifulSoup


class Base(object):

    @staticmethod
    def get_soup(link):
        html = requests.get(link).content
        return BeautifulSoup(html, features='html.parser')

    def get_price_from_link(self, link):
        pass

    def search_product(self, *args, **kwargs):
        pass
    
    pass