from playwright.sync_api import sync_playwright
from login_page import LoginPage
from navigator import Navigator
from find_textbook import FindTextbook, get_textbooks_list
import time

def run(textbook):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto("https://www.pearsonactivelearn.com/app/login")
        nav = Navigator(page)
        login = LoginPage(nav)
        find = FindTextbook(nav)
        login.login()
        login.reject_cookies()          
        find.select_textbook(textbook)
        input() #Freezes page so it dosent close

def get_textbooks():
    return(get_textbooks_list())