from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):

    SHOP_BY_PRODUCT = (By.ID, 'Details-HeaderMenu-2')
    SHOP_BY_PRODUCT_MENU = (By.ID, 'HeaderMenu-MenuList-2')
    SUNSCREENS = (By.XPATH, '//ul[@id="HeaderMenu-MenuList-2"]/li/a[@href="/collections/sun-protection"]')

    def open_main_page(self, end_url=''):
        self.open_url(end_url)

    def click_to_shop_by_product(self):
        self.click(*self.SHOP_BY_PRODUCT)

    def select_sunscreens(self):
        if self.wait_for_element_appear(*self.SHOP_BY_PRODUCT_MENU):
            self.click(*self.SUNSCREENS)