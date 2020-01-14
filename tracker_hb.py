from basetracker import Base
from bs4 import BeautifulSoup
import codecs
from utilities import char_to_hex

class HBTracker(Base):

    SEARCH_QUERY_BASE = 'https://www.hepsiburada.com/ara?q='

    def get_price_from_link(self, link):
        """ <span id='offering-id' content='PRICE' """
        soup = Base.get_soup(link)
        price_tag = soup.find(name='span', id='offering-price')
        return price_tag['content']
