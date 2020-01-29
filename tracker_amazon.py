from basetracker import Base
import time


class AmazonTracker(Base):

    @staticmethod
    def get_price_from_link(link):
        # TODO: SOLVE A PROBLEM, AMAZON WANTS TO SOLVE A CAPTCHA
        soup = Base.get_soup(link)
        price_tag = soup.find(name='span', id='price_inside_buybox')
        print(soup.prettify())
        return str(price_tag.string).strip()

    def construct_search_query(self, query):
        clean_query = [self.SEARCH_QUERY_BASE]
        for ch in query:
            if ch.isalnum():
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


print(AmazonTracker.get_price_from_link("https://www.amazon.com.tr/Samsung-970-500GB-NVMe-MZ-V7E500BW/dp/B07CGGP7SV/ref=sr_1_2?__mk_tr_TR=ÅMÅŽÕÑ&keywords=samsung+ssd&qid=1579389474&sr=8-2"))