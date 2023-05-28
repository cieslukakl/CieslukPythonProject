from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Locators:
    """Lokatory strony user home"""
    MY_PROFILE = (By.XPATH, './/h1[text()="MY PROFILE"]')
    SETTINGS_ICON = (By.XPATH, './/a[@href="/me/settings/"]/span[@class="relative z-1"]')
    PERSONAL_BIO = (By.XPATH, './/div/p[@class="font-sans text-xs text-gray"]')
    USER_ATTRIBUTES_DICT = {
        "WARRIORS_ON_QUEST": (By.XPATH, './/div[text()="Warriors On Quest"]//parent::div//span'),
        "ARMY_SIZE": (By.XPATH, './/div[text()="Army size"]//parent::div//span'),
        "ALLIES": (By.XPATH, './/div[text()="Allies"]//parent::div//span'),
        "ENEMIES": (By.XPATH, './/div[text()="Enemies"]//parent::div//span'),
        "STAKED_WARRIORS": (By.XPATH, './/div[text()="Staked Warriors"]//parent::div//span'),
        "SILVER_COINS": (By.XPATH, './/div[text()="Silver Coins"]//parent::div//span'),
        "IDO_ALLOCATION": (By.XPATH, './/div[text()="IDO Allocation"]//parent::div//span'),
        "REWARD_PTS": (By.XPATH, './/div[text()="Reward pts"]//parent::div//span'),
        "POTIONS": (By.XPATH, './/div[text()="Potions"]//parent::div//span'),
        "WINE": (By.XPATH, './/div[text()="Wine"]//parent::div//span'),
        "BEAST_BLOOD": (By.XPATH, './/div[text()="Beast Blood"]//parent::div//span'),
        # "QUESTS_COMPLETED": (By.XPATH, './/div[text()="Quests Completed"]//parent::div//span')
    }


class UserProfilePage(BasePage):
    """User Profile page with all user details"""

    def _verify_page(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(Locators.MY_PROFILE)))

    def check_personal_bio(self):
        return self.driver.find_element(*Locators.PERSONAL_BIO).text

    def click_settings_icon(self):
        self.driver.find_element(*Locators.SETTINGS_ICON).click()

    def get_warriors_amount(self):
        return self.driver.find_element(*Locators.USER_ATTRIBUTES_DICT["ARMY_SIZE"]).text

    def get_warriors_on_quest_amount(self):
        return self.driver.find_element(*Locators.USER_ATTRIBUTES_DICT["WARRIORS_ON_QUEST"]).text

    def get_all_attributes(self):
        lst = []
        for k, v in Locators.USER_ATTRIBUTES_DICT.items():
            print(*v)
            lst.append(self.driver.find_element(*v))
        return lst

