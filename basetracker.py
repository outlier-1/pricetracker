import requests
from bs4 import BeautifulSoup


class Base(object):

    @staticmethod
    def get_soup(link):
        html = requests.get(link).content
        return BeautifulSoup(html, features='html.parser')

    def construct_search_query(self, query):
        pass

    def get_price_from_link(self, link):
        pass

    def search_product(self, *args, **kwargs):
        pass
    
    def extract_product_properties(self, link):
        pass
