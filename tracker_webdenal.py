from basetracker import Base
from utilities import char_to_hex


class WalTracker(Base):
    URL = 'https://www.webdenal.com'
    SEARCH_QUERY_BASE = 'https://www.webdenal.com/arama.jsp?mysearch_id=&mysearch='

    @staticmethod
    def get_price_from_link(link):
        """ <span id='offering-id' content='PRICE' """
        soup = Base.get_soup(link)
        price_tag = soup.find(name='div', class_='price')
        price = list(price_tag.stripped_strings)
        return f"{price[0]}{price[1]}"

    @staticmethod
    def construct_search_query(query):
        clean_query = [WalTracker.SEARCH_QUERY_BASE]
        for ch in query:
            if ch.isalnum() or ch in ['-', ',', ';', '_']:
                clean_query.append(ch)
            elif ch == ' ':
                clean_query.append('+')
            else:
                clean_query.append(char_to_hex(ch, prefix='%'))
        return "".join(clean_query)

    @staticmethod
    def search_product(query, *args, **kwargs):
        """ Returns the Result Links"""
        search_query_link = WalTracker.construct_search_query(query)
        soup = Base.get_soup(search_query_link)
        response_links = []

        # Search Multiple Classes
        for a in soup.findAll('a', class_='card'):
            response_links.append(WalTracker.URL + a['href'])
        return response_links

    @staticmethod
    def extract_product_properties(product_link):
        soup = Base.get_soup(product_link)
        property_dict = dict()
        # Search Multiple Classes
        table_tag = soup.find(name='table', class_='table-condensed')
        for row in table_tag.find_all(name='tr'):
            property_as_tuple = tuple(row.stripped_strings)
            if len(property_as_tuple) == 2:
                key, value = property_as_tuple
                property_dict[key] = value
        return property_dict

x = WalTracker()
print(x.extract_product_properties("https://www.webdenal.com/kingston-16gb-usb-2-0-dt104-16gb-datatraveler_988807.html"))