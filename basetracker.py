import requests
from bs4 import BeautifulSoup


class Base(object):

    @staticmethod
    def get_soup(link):
        html = requests.get(link).content
        return BeautifulSoup(html, features='html.parser')

    @staticmethod
    def construct_search_query(query):
        pass

    @staticmethod
    def get_price_from_link(self, link):
        pass

    @staticmethod
    def search_product(self, *args, **kwargs):
        pass

    @staticmethod
    def extract_product_properties(self, link):
        pass

