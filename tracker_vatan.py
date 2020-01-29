from basetracker import Base
from utilities import char_to_hex


class VatanTracker(Base):
    URL = 'https://www.vatanbilgisayar.com'
    SEARCH_QUERY_BASE = 'https://www.vatanbilgisayar.com/arama/'

    @staticmethod
    def get_price_from_link(link):
        soup = Base.get_soup(link)
        price_tag = soup.find(name='span', class_='product-list__price')
        return price_tag.string

    @staticmethod
    def construct_search_query(query):
        # Vatan has a primal query system, it can't function properly with special characters.
        # That is why, for now, special characters will be transform into space character.
        clean_query = [VatanTracker.SEARCH_QUERY_BASE]
        for ch in query:
            if ch.isalnum():
                clean_query.append(ch)
            elif ch == ' ':
                clean_query.append(char_to_hex(ch, prefix='%'))
            else:
                # It's a special character, treat it like a space
                clean_query.append(char_to_hex(ch, prefix='%'))
        return "".join(clean_query)

    @staticmethod
    def search_product(query, *args, **kwargs):
        """ Returns the Result Links"""
        search_query_link = VatanTracker.construct_search_query(query)
        soup = Base.get_soup(search_query_link)
        response_links = []

        # Search Multiple Classes
        for a in soup.findAll(name='a', class_='product-list__link'):
            response_links.append(VatanTracker.URL + a['href'])
        return response_links

    @staticmethod
    def extract_product_properties(product_link):
        soup = Base.get_soup(product_link)
        property_dict = dict()
        properties_tag = soup.find(name='ul', class_='pdetail-property-list')
        for row in properties_tag.find_all('li'):
            property_as_tuple = tuple(row.stripped_strings)
            if len(property_as_tuple) == 2:
                key, value = property_as_tuple
                property_dict[key] = value
        return property_dict

