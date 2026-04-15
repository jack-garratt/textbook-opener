from dotenv import load_dotenv
import os

class LoginPage():
    def __init__(self, navigator):
        load_dotenv(override=True)
        self.__navigator = navigator
        self.__email = os.getenv('EMAIL')
        self.__password = os.getenv('PASSWORD')

    def login(self):
        self.__navigator.enter_text("Username", self.__email)
        self.__navigator.enter_text("Password", self.__password)
        self.__navigator.click_button("Sign in")

    def reject_cookies(self):
        self.__navigator.click_button("Reject All")