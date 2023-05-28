import pytest
from pytest_bdd import scenario, given, when, then, parsers
from selenium import webdriver
from pages.login_page import Locators, LoginPage
from pages.user_home_page import UserHomePage

# Constants

ARADENA_LOGIN_PAGE = 'https://game.aradena.io/enter/'
USERNAME = "ALK"
PASSWORD = "alk123"

# Scenarios


@scenario('../feature_files/login.feature', 'Successful Aradena page login')
def test_login_successfull():
    pass


@scenario('../feature_files/login.feature', 'Unsuccessful Aradena page login')
def test_login_unsuccessfull():
    pass

# Fixtures


@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.implicitly_wait(10)
    b.maximize_window()
    yield b
    b.quit()

# Given Steps


@given('I am on Aradena login page')
def enter_login_page(browser):
    browser.get(ARADENA_LOGIN_PAGE)


@given(parsers.parse('I enter {username} and {password}'))
def input_user_credentials(browser, username, password):
    LoginPage(browser).enter_username(username)
    LoginPage(browser).enter_password(password)

# When Steps


@when('I select "Log in" button')
def select_login_button(browser):
    LoginPage(browser).click_log_in()

# Then Steps


@then('I see user home page')
def check_home_screen(browser):
    user_logged_visible = UserHomePage(browser).get_user_login_from_home_page()
    assert user_logged_visible.get_attribute('title') == USERNAME


@then('I see login warning')
def check_warning(browser):
    # There are two different warnings possible, thus two different XPATHS for checking text of warning
    for locator in [Locators.WARNING_FIRST, Locators.WARNING_SECOND]:
        try:
            warning = LoginPage(browser).verify_warning_message(locator[0], locator[1])
        except:
            warning = False
        if warning:
            assert warning.text == locator[-1]


# PRECONDITIONS
def logged_in_precondition(browser):
    browser.get(ARADENA_LOGIN_PAGE)
    LoginPage(browser).enter_username(USERNAME)
    LoginPage(browser).enter_password(PASSWORD)
    LoginPage(browser).click_log_in()
    UserHomePage(browser).wait_for_user_home_page()

