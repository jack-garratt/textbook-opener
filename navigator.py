class Navigator():
    def __init__(self,page):
        self._page = page

    def click_button(self, locator):
        self._page.get_by_role("button", name=locator).click()

    def click_link(self, locator):
        self._page.locator("a", has_text=locator).first.dispatch_event("click")

    def enter_text(self, locator, value):
        self._page.get_by_role("textbox", name=locator).fill(value)

    