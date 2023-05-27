import pytest
from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from test_login import logged_in_precondition
from pages.user_profile_page import UserProfilePage
from pages.user_home_page import UserHomePage


# Constants

# Scenarios

@scenario('../feature_files/user_profile_checks.feature', 'Warriors on quest is less or equal to army size')
def test_user_profile_checks():
    pass


@scenario('../feature_files/user_profile_checks.feature', 'All user attributes are displayed')
def test_user_profile_all_attributes_displayed():
    pass

# Fixtures


@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.maximize_window()
    b.implicitly_wait(10)
    yield b
    b.quit()

# Given Steps


@given('I am logged in to Aradena')
def logged_in(browser):
    logged_in_precondition(browser)

# When Steps


@when('I enter profile page')
def enter_tavern_page(browser):
    UserHomePage(browser).expand_menu()
    UserHomePage(browser).select_profile_from_menu()

# Then Steps


@then('I see Warriors on quest amount is less or equal to Army size')
def compare_amounts_of_warriors(browser):
    warriors_amount = int(UserProfilePage(browser).get_warriors_amount())
    warriors_on_quest_amount = int(UserProfilePage(browser).get_warriors_on_quest_amount())
    assert warriors_on_quest_amount <= warriors_amount


@then('I see all user attributes displayed')
def check_all_user_attributes_displayed(browser):
    assert len(UserProfilePage(browser).get_all_attributes()) == 12
