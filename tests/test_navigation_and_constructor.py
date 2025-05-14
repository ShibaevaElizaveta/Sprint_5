from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from locators.all_locators import *
from test_data.test_data import UserData
import pytest


class TestNavigationAndConstructor:
    @pytest.fixture(autouse=True)
    def setup(self, create_driver):
        self.driver = create_driver
        self.wait = WebDriverWait(self.driver, 15)
        self.user = UserData()

    def login(self):

        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        self.driver.find_element(*LoginPageLocators.login_input).send_keys(self.user.email)
        self.driver.find_element(*LoginPageLocators.password_input).send_keys(self.user.password)
        self.driver.find_element(*LoginPageLocators.login_button).click()
        self.wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    def test_account_navigation(self):

        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.wait.until(EC.element_to_be_clickable(HomePageLocators.account_link)).click()
        self.wait.until(EC.url_contains("/login"))

    def test_constructor_navigation(self):

        self.login()


        self.wait.until(EC.element_to_be_clickable(HomePageLocators.account_link)).click()
        self.wait.until(EC.url_contains("/account"))


        self.wait.until(EC.element_to_be_clickable(HomePageLocators.constructor_tab)).click()
        self.wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))


        self.driver.get("https://stellarburgers.nomoreparties.site/account")
        self.wait.until(EC.element_to_be_clickable(HomePageLocators.logo)).click()
        self.wait.until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))

    @pytest.mark.parametrize("section,expected", [
        (ConstructorPageLocators.buns_section, "Булки"),
        (ConstructorPageLocators.sauces_section, "Соусы"),
        (ConstructorPageLocators.fillings_section, "Начинки")
    ])
    def test_constructor_sections(self, section, expected):

        self.driver.get("https://stellarburgers.nomoreparties.site/")


        element = self.wait.until(EC.element_to_be_clickable(section))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(self.driver).move_to_element(element).click().perform()


        active_tab = self.wait.until(
            EC.visibility_of_element_located(ConstructorPageLocators.active_tab)
        )
        assert expected in active_tab.text