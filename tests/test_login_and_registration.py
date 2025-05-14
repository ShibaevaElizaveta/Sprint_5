from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.all_locators import *
from helpers.data_helpers import DataHelpers
from test_data.test_data import UserData
import pytest


class TestLoginAndRegistration:
    @pytest.fixture(autouse=True)
    def setup(self, create_driver):
        self.driver = create_driver
        self.wait = WebDriverWait(self.driver, 15)
        self.data = DataHelpers()
        self.user = UserData()

    def test_successful_registration(self):

        self.driver.get("https://stellarburgers.nomoreparties.site/register")


        name = "TestUser"
        email = self.data.generate_login()
        password = self.data.generate_password()


        self.wait.until(EC.visibility_of_element_located(RegistrationPageLocators.name_input)).send_keys(name)
        self.driver.find_element(*RegistrationPageLocators.email_input).send_keys(email)
        self.driver.find_element(*RegistrationPageLocators.password_input).send_keys(password)
        self.driver.find_element(*RegistrationPageLocators.register_button).click()


        self.wait.until(EC.url_contains("/login"))

    def test_invalid_password_registration(self):

        self.driver.get("https://stellarburgers.nomoreparties.site/register")

        self.driver.find_element(*RegistrationPageLocators.name_input).send_keys("TestUser")
        self.driver.find_element(*RegistrationPageLocators.email_input).send_keys("test@example.com")
        self.driver.find_element(*RegistrationPageLocators.password_input).send_keys("123")
        self.driver.find_element(*RegistrationPageLocators.register_button).click()


        error = self.wait.until(EC.visibility_of_element_located(RegistrationPageLocators.error_message))
        assert "Некорректный пароль" in error.text

    @pytest.mark.parametrize("entry_point,start_page", [
        (HomePageLocators.login_account_button, "/"),
        (HomePageLocators.account_link, "/"),
        (RegistrationPageLocators.account_link, "/register"),
        (LoginPageLocators.account_link, "/forgot-password")
    ])
    def test_login_from_different_points(self, entry_point, start_page):

        self.driver.get(f"https://stellarburgers.nomoreparties.site{start_page}")
        self.wait.until(EC.element_to_be_clickable(entry_point)).click()
        self.wait.until(EC.url_contains("/login"))


        self.driver.find_element(*LoginPageLocators.login_input).send_keys(self.user.email)
        self.driver.find_element(*LoginPageLocators.password_input).send_keys(self.user.password)
        self.driver.find_element(*LoginPageLocators.login_button).click()


        self.wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    def test_logout(self):

        self.driver.get("https://stellarburgers.nomoreparties.site/login")


        self.driver.find_element(*LoginPageLocators.login_input).send_keys(self.user.email)
        self.driver.find_element(*LoginPageLocators.password_input).send_keys(self.user.password)
        self.driver.find_element(*LoginPageLocators.login_button).click()


        self.wait.until(EC.element_to_be_clickable(HomePageLocators.account_link)).click()
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.login_button)).click()
        self.wait.until(EC.url_contains("/login"))