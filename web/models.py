from flask_login import UserMixin


class User(UserMixin):

    id = "1"
    email = "user@domain.com"
    password = "password"
    name = "Sean J Person"
    type = "Patient"
    birth_day = "24/05/1983"
    gender = "hombre"
    address = "1403 Godfrey Street OR"
    phone = "503-622-2975"

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password
