import random
import string

class DataHelpers:
    @staticmethod
    def generate_login() -> str:
        login_length = random.randint(3, 10)
        login = ''.join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(login_length)
        )
        domains = ["ya.ru", "mail.ru", "gmail.com", "yandex.com"]
        return f"{login}@{random.choice(domains)}".lower()

    @staticmethod
    def generate_password(min_length=6, max_length=12) -> str:
        length = random.randint(min_length, max_length)
        return ''.join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(length)
        )
