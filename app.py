from playwright.sync_api import sync_playwright
from login_page import LoginPage
from navigator import Navigator
from find_textbook import FindTextbook
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.pearsonactivelearn.com/app/login")
        nav = Navigator(page)
        login = LoginPage(nav)
        find = FindTextbook(nav)
        login.login()
        login.reject_cookies()
        time.sleep(50)
run()