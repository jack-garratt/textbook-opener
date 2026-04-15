class Navigator():
    def __init__(self,page):
        self.__page = page

    def click_button(self, locator):
        self.__page.get_by_role("button", name=locator).click()

    def enter_text(self, locator, value):
        self.__page.get_by_role("textbox", name=locator).fill(value)