from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.all_locators import *
from helpers.data_helpers import DataHelpers
from test_data.test_data import UserData,Urls
import pytest

@pytest.mark.usefixtures("setup")
class TestLoginAndRegistration:

    def test_successful_registration(self):

        self.driver.get(Urls.register)

        name = "TestUser"
        email = self.data.generate_login()
        password = self.data.generate_password()


        self.wait.until(EC.visibility_of_element_located(RegistrationPageLocators.name_input)).send_keys(name)
        self.driver.find_element(*RegistrationPageLocators.email_input).send_keys(email)
        self.driver.find_element(*RegistrationPageLocators.password_input).send_keys(password)
        self.driver.find_element(*RegistrationPageLocators.register_button).click()


        self.wait.until(EC.url_contains("/login"))

        self.driver.find_element(*LoginPageLocators.login_input).send_keys(email)
        self.driver.find_element(*LoginPageLocators.password_input).send_keys(password)
        self.driver.find_element(*LoginPageLocators.login_button).click()
        order_button = self.wait.until(
            EC.visibility_of_element_located(HomePageLocators.order_button)
        )
        assert self.driver.current_url == Urls.home_page, \
            "Пользователь был перенаправлен на главную страницу после входа"

        assert order_button.text == "Оформить заказ", \
            f"Текст кнопки совпадает. получено: '{order_button.text}'"

    def test_invalid_password_registration(self):

        self.driver.get(Urls.register)

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


        self.wait.until(EC.url_to_be(Urls.home_page))

        order_button = self.wait.until(
            EC.visibility_of_element_located(HomePageLocators.order_button)
        )

        assert order_button.text == "Оформить заказ", \
            f"Текст кнопки совпадает. получено: '{order_button.text}'"

    @pytest.mark.usefixtures("authorized_driver")
    def test_logout(self):
        self.wait.until(EC.element_to_be_clickable(HomePageLocators.account_link)).click()
        self.wait.until(EC.element_to_be_clickable(AccountPageLocators.logout_button)).click()
        self.wait.until(EC.url_contains("/login"))
        login_button = self.wait.until(
            EC.visibility_of_element_located(LoginPageLocators.login_button)
        )
        assert login_button.text == "Войти", \
            f"Текст кнопки совпадает. получено: '{login_button.text}'"