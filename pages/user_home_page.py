from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators:
    """Lokatory strony user home"""
    USER_LOGIN = (By.XPATH, './/span[@title="ALK"]')
    MENU_BUTTON = (By.XPATH, './/button[@title="Menu"]')
    TAVERN_SUBPAGE = (By.XPATH, './/a[@href="/tavern/"]')
    PROFILE_SUBPAGE = (By.XPATH, './/nav/div/a[@href="/me/"]')


class UserHomePage(BasePage):
    """Strona logowania"""

    def _verify_page(self):
        wait = WebDriverWait(self.driver,3)
        wait.until((EC.visibility_of_element_located(Locators.USER_LOGIN)))

    def get_user_login_from_home_page(self):
        return self.driver.find_element(*Locators.USER_LOGIN)

    def expand_menu(self):
        self.driver.find_element(*Locators.MENU_BUTTON).click()

    def select_tavern_from_menu(self):
        self.driver.find_element(*Locators.TAVERN_SUBPAGE).click()

    def select_profile_from_menu(self):
        self.driver.find_element(*Locators.PROFILE_SUBPAGE).click()
