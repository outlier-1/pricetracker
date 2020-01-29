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
        return price_tag['content']

    @staticmethod
    def construct_search_query(query):
        clean_query = [HBTracker.SEARCH_QUERY_BASE]
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
        search_query_link = HBTracker.construct_search_query(query)
        soup = Base.get_soup(search_query_link)
        response_links = []

        # Search Multiple Classes
        for product_div in soup.findAll(recursive=True, attrs={'class': ['box', 'product']}, limit=5):
            response_links.append(HBTracker.URL + product_div.a['href'])
        return response_links

    @staticmethod
    def extract_product_properties(product_link):
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

print(HBTracker.get_price_from_link("https://www.hepsiburada.com/rastar-r-c-1-18-ferrari-f138-uzaktan-kumandali-formula-1-arabasi-p-HBV000007OU4P?magaza=İnternet%20Oyuncak"))