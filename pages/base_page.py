from playwright.sync_api import Page, expect, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page