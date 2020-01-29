from tracker_hb import HBTracker
from tracker_vatan import VatanTracker
from tracker_amazon import AmazonTracker
from tracker_webdenal import WalTracker


class Tracker:

    def __init__(self, user):
        if user is None:
            raise ValueError('Tracker must have a User Class Instance to be assigned.\n'
                             f'Type of given parameter {type(user)},\nIt Should be User')

        self.tracked_products = {
            'amazon': [],
            'hepsiburada': [],
            'vatan': [],
            'webdenal': [],
        }

    @staticmethod
    def track_new_product(self, product):
        pass

    @classmethod
    def get_price_from_link(cls, link):
        pass

    @classmethod
    def construct_search_query(query):
        pass

    @classmethod
    def search_product(query, *args, **kwargs):
        pass

    @classmethod
    def extract_product_properties(product_link):
        pass
