from pages.main_page import Page
from selenium.webdriver.common.by import By

class SearchPage(Page):

    ITEMS_NAME = (By.CSS_SELECTOR, '.full-unstyled-link')
    ITEMS_IMAGE = (By.CSS_SELECTOR, 'img.motion-reduce')
    ITEMS_PRICE = (By.CSS_SELECTOR, '.price-item.price-item--sale.price-item--last')

    def open_page_with_end_url(self, end_url):
        self.open_url(end_url)

    def verify_1st_item_name(self):
        items = self.find_elements(*self.ITEMS_NAME)
        assert items[0].text, f'Error! First item dose not have text'

    def verify_1st_item_image(self):
        items = self.find_elements(*self.ITEMS_IMAGE)
        assert items[0].is_displayed, f'Error! First item dose not have image'

    def verify_1st_item_price(self):
        items = self.find_elements(*self.ITEMS_PRICE)
        price = items[0].text
        assert not price.index('Rs. ') and price[4:-3].isnumeric(), f'Error! First item dose not have prise'


