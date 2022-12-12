from pages.collections_page import Collections

class Face(Collections):

    def verify_header(self):
        super().verify_header('Face')

    def verify_1st_product(self):
        super().verify_1st_product(super().PRODUCTS, 'face')