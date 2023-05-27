from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators:
    """Lokatory strony logowania"""
    USERNAME_INPUT = (By.XPATH, '//*[@id="login-username"]/div/input')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="login-password"]/div/input')
    LOGIN_BUTTON = (By.XPATH, './/button[@title="Log in"]')
    WARNING_FIRST = (By.XPATH, './/p[@class="text-shadow-xs-weak font-sans text-xs font-medium leading-normal text-white"]',"User credentials are not valid")
    WARNING_SECOND = (By.XPATH, './/span[@class="text-red-lighter"]', "Incorrect username or password")


class LoginPage(BasePage):
    """Login page"""

    def _verify_page(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until((EC.visibility_of_element_located(Locators.USERNAME_INPUT)))
        wait.until((EC.visibility_of_element_located(Locators.PASSWORD_INPUT)))

    def enter_username(self, username):
        """Enters username"""
        el = self.driver.find_element(*Locators.USERNAME_INPUT)
        el.send_keys(username)

    def enter_password(self, password):
        """Enters password"""
        el = self.driver.find_element(*Locators.PASSWORD_INPUT)
        el.send_keys(password)

    def click_log_in(self):
        """Clicks Log in"""
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()

    def verify_warning_message(self, method, xpath):
        """Finds warning"""
        return self.driver.find_element(method, xpath)
