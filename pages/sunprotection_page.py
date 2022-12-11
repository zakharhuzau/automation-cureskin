from pages.base_page import Page
from selenium.webdriver.common.by import By

class SunProtection(Page):

    HEADER = (By.CSS_SELECTOR, '.collection-hero__title')
    HEADER_HIDDEN = (By.XPATH, '//h1/span[@class="visually-hidden"]')
    PRODUCTS = (By.CSS_SELECTOR, '.full-unstyled-link')

    def verify_header(self):
        css_value = self.find_element(*self.HEADER_HIDDEN).value_of_css_property('position')
        if css_value == 'absolute':
            header = 'Collection:\nSun Protection'
        else:
            header = 'Sun Protection'
        self.verify_element_text(header, *self.HEADER)

    def verify_1st_product(self):
        products = self.find_elements(*self.PRODUCTS)
        assert products[0].text.lower().find('sunscreen') >= 0, \
            f'Error! "sunscreen" does not contain in "{products[0].text}"'