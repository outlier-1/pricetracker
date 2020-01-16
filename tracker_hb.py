from basetracker import Base
from utilities import char_to_hex


class HBTracker(Base):

    URL = 'https://www.hepsiburada.com'
    SEARCH_QUERY_BASE = 'https://www.hepsiburada.com/ara?q='

    @staticmethod
    def get_price_from_link(link):
        """ <span id='offering-id' content='PRICE' """
        soup = Base.get_soup(link)
        price_tag = soup.find(name='span', id='offering-price')
        formatted_price = "{:,.2f}".format(float(price_tag['content']))
        return formatted_price

    @staticmethod
    def construct_search_query(query):
        clean_query = [HBTracker.SEARCH_QUERY_BASE]
        valid_chars = ['-', '_', '*']
        for ch in query:
            if ch.isalnum() or ch in valid_chars:
                clean_query.append(ch)
            elif ch == ' ':
                clean_query.append('+')
            else:
                clean_query.append(char_to_hex(ch,prefix='%'))
        return "".join(clean_query)

    def search_product(self, query, *args, **kwargs):
        """ Returns the Result Links"""
        search_query_link = self.construct_search_query(query)
        soup = Base.get_soup(search_query_link)
        print(search_query_link)
        response_links = []

        # Search Multiple Classes
        for product_div in soup.findAll(recursive=True, attrs={'class': ['box', 'product']}, limit=5):
            response_links.append(self.URL + product_div.a['href'])
        print(response_links)

    def extract_product_properties(self, product_link):
        soup = Base.get_soup(product_link)
        property_dict = dict()
        key, value = None, None
        # Search Multiple Classes
        for table in soup.find_all(recursive=True, attrs={'class': ['data-list', 'tech-spec']}):
            for index, info in enumerate(list(table.stripped_strings)):
                if info == 'Diğer':
                    break
                if index % 2 == 0:
                    key = info
                else:
                    value = info
                    property_dict[key] = value
        return property_dict
