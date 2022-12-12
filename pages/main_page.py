from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):

    SHOP_BY_PRODUCT = (By.ID, 'Details-HeaderMenu-2')
    SHOP_BY_CATEGORY = (By.ID, 'Details-HeaderMenu-3')
    SHOP_BY_PRODUCT_MENU = (By.ID, 'HeaderMenu-MenuList-2')
    SHOP_BY_CATEGORY_MENU = (By.ID, 'HeaderMenu-MenuList-3')
    SUNSCREENS = (By.XPATH, '//ul[@id="HeaderMenu-MenuList-2"]/li/a[@href="/collections/sun-protection"]')
    FACE = (By.XPATH, '//ul[@id="HeaderMenu-MenuList-3"]/li/a[@href="/collections/face"]')

    def open_main_page(self, end_url=''):
        self.open_url(end_url)

    def click_to_shop_by_product(self):
        self.click(*self.SHOP_BY_PRODUCT)

    def select_sunscreens(self):
        if self.wait_for_element_appear(*self.SHOP_BY_PRODUCT_MENU):
            self.click(*self.SUNSCREENS)

    def click_to_shop_by_category(self):
        self.click(*self.SHOP_BY_CATEGORY)

    def select_face(self):
        if self.wait_for_element_appear(*self.SHOP_BY_CATEGORY_MENU):
            self.click(*self.FACE)