from dataclasses import dataclass

@dataclass
class UserData:
    name: str = 'Elizaveta'
    email: str = 'elizaveta_shibaeva_22_123@yandex.ru'
    password: str = 'qwerty_22'
    invalid_password: str = '123'
