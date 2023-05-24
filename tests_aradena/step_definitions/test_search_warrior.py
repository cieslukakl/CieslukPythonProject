import pytest
import time
from pytest_bdd import scenario, given, when, then, parsers
from selenium import webdriver
from test_login import logged_in_precondition
from pages.tavern_page import TavernPage, Locators
from pages.user_home_page import UserHomePage
from utils import Utils
from pages.tavern_page import FilterMapper


# Constants

# Scenarios

@scenario('../feature_files/search_warrior.feature', 'Successfull search for warrior in tavern')
def test_warrior_search_successfull():
    pass


@scenario('../feature_files/search_warrior.feature', 'Unsuccessful search for warrior in tavern')
def test_warrior_search_unsuccessfull():
    pass

@scenario('../feature_files/search_warrior.feature', 'Successfull search for warrior in tavern (RANDOM)')
def test_warrior_search_successfull_random():
    pass

#Fixtures

@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.maximize_window()
    b.implicitly_wait(3)
    yield b
    b.quit()

# Given Steps

@given('I am logged in to Aradena')
def logged_in(browser):
    logged_in_precondition(browser)


@given('I enter tavern (Browse Warriors) page')
def enter_tavern_page(browser):
    UserHomePage(browser).expand_menu()
    UserHomePage(browser).select_tavern_from_menu()


@given(parsers.parse('I select Filter By {collection}'))
def filter_collection(browser, collection):
    TavernPage(browser).select_collection_filter(collection)


@given('I Filter By male or female')
def filter_collection_random(browser):
    collection = Utils().get_random_collection_filter(FilterMapper.CollectionFilterDict)
    TavernPage(browser).select_collection_filter(collection)


@given(parsers.parse('I input warrior {warriorId}'))
def input_warrior_id(browser, warriorId):
    TavernPage(browser).enter_warrior_id(warriorId)


@given('I input 1 random valid warior ID')
def input_random_warrior_id(browser):
    warriorId = Utils().get_random_warrior_id()
    TavernPage(browser).enter_warrior_id(warriorId)

# When Steps


@when('I select Submit button')
def select_submit_button(browser):
    TavernPage(browser).click_submit_button()
    time.sleep(3)
# Then Steps


@then(parsers.parse('I can see {number} of warriors found'))
def check_displayed_warriors(browser, number):
    assert TavernPage(browser).find_displayed_warriors() == number


@then('I can see 1 warrior found')
def check_displayed_warrior(browser):
    assert TavernPage(browser).find_displayed_warriors() == str(1)


@then(parsers.parse('I can see "No warriors found" message'))
def check_no_warriors_displayed(browser):
    assert TavernPage(browser).check_warriors_not_found_message() == True

