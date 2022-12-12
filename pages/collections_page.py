from pages.main_page import Page
from selenium.webdriver.common.by import By

class Collections(Page):

    HEADER = (By.CSS_SELECTOR, '.collection-hero__title')
    HEADER_HIDDEN = (By.XPATH, '//h1/span[@class="visually-hidden"]')
    PRODUCTS = (By.CSS_SELECTOR, '.full-unstyled-link')

    def verify_header(self, text):
        css_value = self.find_element(*self.HEADER_HIDDEN).value_of_css_property('position')
        if css_value == 'absolute':
            header = f'Collection:\n{text}'
        else:
            header = text
        self.verify_element_text(header, *self.HEADER)

    def verify_1st_product(self, locator, text):
        products = self.find_elements(*locator)
        assert products[0].text.lower().find(text) >= 0, \
            f'Error! "{text}" does not contain in "{products[0].text}"'