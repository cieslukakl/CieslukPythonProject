from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Locators:
    """Lokatory strony user home"""
    ACCOUNT_SETTINGS = (By.XPATH, './/h1[text()="Account Settings"]')
    PERSONAL_BIO_INPUT = (By.XPATH, './/textarea[@placeholder = "Personal Bio"]')
    SAVE_BUTTON = (By.XPATH, './/button[@type="submit"]/span[text()="Save "]')
    SUCCESS_NOTIFICATION = (By.XPATH, './/p[text()="Changes successfully saved!"]')
    BACK_BUTTON = (By.XPATH, './/div[@class="mb-10 flex flex-wrap items-center justify-between sm:flex-nowrap"]/button[@type="button"]/span[@class="relative z-1"]/span[@class="nuxt-icon"]')


class SettingsPage(BasePage):

    def _verify_page(self):
        wait = WebDriverWait(self.driver,3)
        wait.until((EC.visibility_of_element_located(Locators.ACCOUNT_SETTINGS)))

    def enter_personal_bio(self, faker_data):
        el = self.driver.find_element(*Locators.PERSONAL_BIO_INPUT)
        el.send_keys(Keys.COMMAND + "a")
        el.send_keys(Keys.DELETE)
        el.send_keys(faker_data)

    def select_save_button(self):
        self.driver.find_element(*Locators.SAVE_BUTTON).click()

    def check_successfull_change_notification(self):
        return bool(self.driver.find_element(*Locators.SUCCESS_NOTIFICATION))

    def click_back_button(self):
        return self.driver.find_element(*Locators.BACK_BUTTON).click()

