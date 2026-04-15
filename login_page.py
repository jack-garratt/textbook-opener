import os

class LoginPage():
    def __init__(self, navigator):
        self._navigator = navigator
        self._email = os.getenv('EMAIL')
        self._password = os.getenv('PASSWORD')

    def login(self):
        self._navigator.enter_text("Username", self._email)
        self._navigator.enter_text("Password", self._password)
        self._navigator.click_button("Sign in")

    def reject_cookies(self):
        self._navigator.click_button("Reject All")