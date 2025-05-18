from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from locators.all_locators import *
from test_data.test_data import UserData, Urls
import pytest

class TestNavigationAndConstructor:
    @pytest.fixture(autouse=True)
    def setup(self, create_driver):
        self.driver = create_driver
        self.wait = WebDriverWait(self.driver, 15)
        self.user = UserData()

    @pytest.mark.usefixtures("authorized_driver")
    def test_account_navigation(self):
        self.driver.get(Urls.home_page)
        self.wait.until(EC.element_to_be_clickable(HomePageLocators.account_link)).click()

        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile", \
            "Пользователь был перенаправлен в личный кабинет"

    @pytest.mark.usefixtures("authorized_driver")
    def test_constructor_navigation(self):
        self.wait.until(EC.element_to_be_clickable(HomePageLocators.account_link)).click()
        self.wait.until(EC.url_contains("/account"))

        self.wait.until(EC.element_to_be_clickable(HomePageLocators.constructor_tab)).click()
        self.wait.until(EC.url_to_be(Urls.home_page))

        assert self.driver.current_url == Urls.home_page, \
        "Пользователь был перенаправлен на главную страницу"

    @pytest.mark.usefixtures("authorized_driver")
    def test_logo_navigation(self):
        self.driver.get(Urls.account)
        self.wait.until(EC.element_to_be_clickable(HomePageLocators.logo)).click()
        self.wait.until(EC.url_to_be(Urls.home_page))

        assert self.driver.current_url == Urls.home_page, \
        "Пользователь был перенаправлен на главную страницу"

    @pytest.mark.parametrize("section,expected", [
        (ConstructorPageLocators.buns_section, "Булки"),
        (ConstructorPageLocators.sauces_section, "Соусы"),
        (ConstructorPageLocators.fillings_section, "Начинки")
    ])
    def test_constructor_sections(self, section, expected):
        self.driver.get(Urls.home_page)

        element = self.wait.until(EC.element_to_be_clickable(section))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        ActionChains(self.driver).move_to_element(element).click().perform()

        active_tab = self.wait.until(
            EC.visibility_of_element_located(ConstructorPageLocators.active_tab)
        )
        assert expected in active_tab.text