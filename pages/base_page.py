

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()
        # bedzie automatycznie uruchamiana podczas tworzenia tej strony

    def _verify_page(self):
    # site autotest
        return