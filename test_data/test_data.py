from dataclasses import dataclass

@dataclass
class UserData:
    name: str = 'Elizaveta'
    email: str = 'elizaveta_shibaeva_22_123@yandex.ru'
    password: str = 'qwerty_22'
    invalid_password: str = '123'

@dataclass
class Urls:
    home_page = "https://stellarburgers.nomoreparties.site/"
    login_page = "https://stellarburgers.nomoreparties.site/login"
    account_profile = "https://stellarburgers.nomoreparties.site/account/profile"
    account = "https://stellarburgers.nomoreparties.site/account"
    register = "https://stellarburgers.nomoreparties.site/register"
    forgot_password = "https://stellarburgers.nomoreparties.site/forgot-password"