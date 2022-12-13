from pages.main_page import MainPage
from pages.sunprotection_page import SunProtection
from pages.face_page import Face
from pages.search_page import SearchPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.sunprotection_page = SunProtection(self.driver)
        self.face_page = Face(self.driver)
        self.search_page = SearchPage(self.driver)