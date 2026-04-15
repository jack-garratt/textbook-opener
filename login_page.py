from dotenv import load_dotenv
import os

class LoginPage():
    def __init__(self, navigator):
        load_dotenv()
        self.__navigator = navigator
        self.__email = os.getenv('EMAIL')
        self.__password = os.getenv('PASSWORD')
    