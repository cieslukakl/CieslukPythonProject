from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage():
    """
    Base class used by other pages
    """
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()
        self.alert = Alert(self.driver)

    def _verify_page(self):
        """Autotest strony - utuchamiany automatycznie po wej\u015bciu na ni\u0105"""
        return