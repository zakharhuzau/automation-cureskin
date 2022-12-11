from pages.main_page import MainPage
from pages.sunprotection_page import SunProtection

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.sunprotection_page = SunProtection(self.driver)