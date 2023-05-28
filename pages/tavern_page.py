from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import Utils


class FilterMapper:
    CollectionFilterDict = {
        "AllCollections": "null-0",
        "Male": "null-1",
        "Female": "null-2"
    }
    CollectionURLFilterDict = {
        "Male": "/1/",
        "Female": "/2/",
        "AllCollections": "/1/"
    }


class Locators:
    """Lokatory strony logowania"""
    MENU_BUTTON = (By.XPATH, './/button[@title="Menu"]')
    EXPLORE_WARRIORS = (By.XPATH, './/button[text()="explore warriors"]')
    FILTER_BY_COLLECTION = (By.XPATH, './/span[text()="Filter by:"]')
    FILTER_XPATH = './/div[@class="multiselect__content-wrapper" and @style="max-height: 300px;"]/ul/li[@id="null-0"]'
    FILTER_XPATH_REPLACE_STRING = "null-0"
    SEARCH_FIELD = (By.XPATH, './/input[@placeholder="SEARCH"]')
    SUBMIT_BUTTON = (By.XPATH, './/button[@type="submit"]')
    WARRIOR_FOUND = (By.XPATH, '//div[@class = "flex items-start"]/div/a')
    SPECIFIC_WARRIOR_FOUND = './/div[@class = "flex items-start"]/div/a[@href = "/tavern/warrior/1/3183"]'
    WARRIOR_NOT_FOUND = (By.XPATH, '//h2[text() = "No Warriors Found"]')


class TavernPage(BasePage):
    """Tavern page"""

    def _verify_page(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(Locators.EXPLORE_WARRIORS)))

    def select_collection_filter(self, collection):
        """Filters collection"""
        self.driver.find_element(*Locators.FILTER_BY_COLLECTION).click()
        collection_xpath = Utils().create_xpath(Locators.FILTER_XPATH, Locators.FILTER_XPATH_REPLACE_STRING,
                                                FilterMapper.CollectionFilterDict[collection])
        self.driver.find_element(By.XPATH, collection_xpath).click()

    def select_collection_filter_random(self):
        """Filters collection"""
        self.driver.find_element(*Locators.FILTER_BY_COLLECTION).click()
        collection = Utils().get_random_collection_filter(FilterMapper.CollectionFilterDict)
        collection_xpath = Utils().create_xpath(Locators.FILTER_XPATH, Locators.FILTER_XPATH_REPLACE_STRING,
                                                FilterMapper.CollectionFilterDict[collection])
        self.driver.find_element(By.XPATH, collection_xpath).click()

    def enter_warrior_id(self, warriorId):
        """Enters warrior ID"""
        el = self.driver.find_element(*Locators.SEARCH_FIELD)
        el.send_keys(warriorId)

    def click_submit_button(self):
        """Clicks Submit button"""
        self.driver.find_element(*Locators.SUBMIT_BUTTON).click()

    def find_displayed_warriors(self, collection, warriorId):
        """Searches for displayed warriors"""
        specific_warrior_xpath = Utils().create_xpath_warrior(Locators.SPECIFIC_WARRIOR_FOUND, warriorId,
                                                              FilterMapper.CollectionURLFilterDict[collection])
        self.wait_for_element((By.XPATH, specific_warrior_xpath))
        return str(len(self.driver.find_elements(*Locators.WARRIOR_FOUND)))

    def check_warriors_not_found_message(self):
        """Searches for warriors not found message"""
        self.wait_for_element(Locators.WARRIOR_NOT_FOUND)
        return bool(self.driver.find_element(*Locators.WARRIOR_NOT_FOUND))

    def wait_for_element(self, element):
        wait = WebDriverWait(self.driver, 5)
        wait.until((EC.visibility_of_element_located(element)))

