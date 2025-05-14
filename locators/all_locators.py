from selenium.webdriver.common.by import By

class HomePageLocators:
    login_account_button = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    account_link = (By.XPATH, "//a[@href='/account']")                        # Ссылка "Личный кабинет"
    constructor_tab = (By.XPATH, "//p[text()='Конструктор']")                 # Вкладка "Конструктор"
    logo = (By.CSS_SELECTOR, "div[class^='AppHeader_header__logo']")             # Логотип Stellar Burgers
    logo = (By.CSS_SELECTOR, "div[class^='AppHeader_header__logo']")             # Логотип Stellar Burgers

class LoginPageLocators:
    login_label = (By.XPATH, "//h2[text()='Вход']")                          # Заголовок "Вход"
    login_input = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # Поле Email
    password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле Пароль
    login_button = (By.XPATH, "//button[text()='Войти']")                     # Кнопка "Войти"
    registration_link = (By.XPATH, "//a[@href='/register']")                  # Ссылка "Зарегистрироваться"
    account_link = (By.XPATH, "//a[@href='/account']")
    restore_password_link = (By.XPATH, "//a[@href='/forgot-password']")       # Ссылка "Восстановить пароль"

class RegistrationPageLocators:
    name_input = (By.XPATH, "//label[text()='Имя']/following-sibling::input")    # Поле Имя
    email_input = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Поле Email
    password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле Пароль
    register_button = (By.XPATH, "//button[text()='Зарегистрироваться']")        # Кнопка "Зарегистрироваться"
    account_link = (By.XPATH, "//a[@href='/account']")
    error_message = (By.XPATH, "//p[contains(@class, 'input__error')]")          # Сообщение об ошибке

class AccountPageLocators:
    name_input = (By.XPATH, "//label[text()='Имя']/following-sibling::input")    # Поле Имя в ЛК
    login_input = (By.XPATH, "//label[text()='Логин']/following-sibling::input") # Поле Логин в ЛК
    password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")  # Поле Пароль в ЛК
    login_button = (By.XPATH, "//button[text()='Выход']")                       # Кнопка "Выход" (logout)

class ConstructorPageLocators:
    buns_section = (By.XPATH, "//span[text()='Булки']/..")                      # Раздел "Булки"
    sauces_section = (By.XPATH, "//span[text()='Соусы']/..")                    # Раздел "Соусы"
    fillings_section = (By.XPATH, "//span[text()='Начинки']/..")                # Раздел "Начинки"
    active_tab = (By.XPATH, "//div[contains(@class, 'current')]")               # Активный раздел