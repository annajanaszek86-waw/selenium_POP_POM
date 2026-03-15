from tests.base_test import BaseTest

class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        #odwołanie się do klasy  nadrzędnej z base_test
        self.home_page.click_sign_in()
        
    def testNoSurname(self):
        pass

