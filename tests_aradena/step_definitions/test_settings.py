import pytest
from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from test_login import logged_in_precondition
from pages.settings_page import SettingsPage
from pages.user_profile_page import UserProfilePage
from pages.user_home_page import UserHomePage
from utils import Utils
from faker import Faker

# Constants

# Scenarios


@scenario('../feature_files/settings.feature', 'Successfull personal bio change')
def test_setting_personal_bio():
    pass

# Fixtures


@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.maximize_window()
    b.implicitly_wait(10)
    yield b
    b.quit()


@pytest.fixture
def data_from_faker():
    return ""

# Given Steps


@given('I am logged in to Aradena')
def logged_in(browser):
    logged_in_precondition(browser)


@given('I enter profile page')
def enter_tavern_page(browser):
    UserHomePage(browser).expand_menu()
    UserHomePage(browser).select_profile_from_menu()


@given('I select Settings icon')
def select_settings(browser):
    UserProfilePage(browser).click_settings_icon()


@given('I input faker values for Personal bio', target_fixture="data_from_faker")
def input_faker_values_into_personal_bio(browser):
    faker_data = Faker().text()
    SettingsPage(browser).enter_personal_bio(faker_data)
    return faker_data


# When Steps


@when('I select Save button')
def select_save_button(browser):
    SettingsPage(browser).select_save_button()
# Then Steps


@then('I can see Success notification')
def check_success_notification(browser):
    assert SettingsPage(browser).check_successfull_change_notification() == True


@then('Personal bio is updated on profile page')
def verify_new_personal_bio(browser, data_from_faker):
    SettingsPage(browser).click_back_button()
    faker_data_from_page = UserProfilePage(browser).check_personal_bio()
    assert Utils().standarize_text(faker_data_from_page) == Utils().standarize_text(data_from_faker)
