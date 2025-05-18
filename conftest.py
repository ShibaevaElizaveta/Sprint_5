import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators.all_locators import LoginPageLocators
from test_data.test_data import UserData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.data_helpers import DataHelpers

@pytest.fixture(scope="function")
def create_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def setup(request, create_driver):
    request.cls.driver = create_driver
    request.cls.wait = WebDriverWait(create_driver, 15)
    request.cls.user = UserData()
    request.cls.data = DataHelpers()

@pytest.fixture
def user():
    return UserData()

@pytest.fixture
def authorized_driver(create_driver, user):
    driver = create_driver
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*LoginPageLocators.login_input).send_keys(user.email)
    driver.find_element(*LoginPageLocators.password_input).send_keys(user.password)
    driver.find_element(*LoginPageLocators.login_button).click()
    WebDriverWait(driver, 15).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
    return driver