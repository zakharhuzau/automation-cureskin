from pages.collections_page import Collections
from selenium.webdriver.common.by import By

class SunProtection(Collections):

    def verify_header(self):
        super().verify_header('Sun Protection')

    def verify_1st_product(self):
        super().verify_1st_product(super().PRODUCTS, 'sunscreen')