from pages.base_page import BasePage
from playwright.sync_api import Page
from utils.config_reader import get_property

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.link_login = page.locator("//a[text()='LOGIN' ]")

    def open(self)-> "HomePage":
        url = get_property("base_url")
        self.page.goto(url)
        return self

    def click_link_login(self) -> None:

        self.link_login.click()