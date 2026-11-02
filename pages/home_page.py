from pages.base_page import BasePage
from playwright.sync_api import Page


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.link_login = page.locator("//a[text()='LOGIN' ]")

    def open(self)-> "HomePage":
        url ="https://telranedu.web.app/home"
        self.page.goto(url)
        return self

    def click_link_login(self) -> None:

        self.link_login.click()