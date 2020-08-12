from Environment.init import Init


def login_param():
    param = {
        'username': Init.username,
        'password': Init.password
    }
    return param


def signup_param():
    param = {
        "name": "ram",
        "email": "init123@gmail.com",
        "password": "init123"
    }
    return param
