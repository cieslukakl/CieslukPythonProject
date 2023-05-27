from selenium.webdriver.common.alert import Alert


class BasePage:
    """
    Base class used by other pages
    """
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()
        self.alert = Alert(self.driver)

    def _verify_page(self):
        """To implement in the future once such need occurs"""
        return
