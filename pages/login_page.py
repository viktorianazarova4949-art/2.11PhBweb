from pages.base_page import BasePage
from playwright.sync_api import Page
from models.user import User

class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.input_email = page.locator("input[name='email']")
        self.input_password = page.locator("input[name='password']")
        self.btn_login = page.locator("//button[text()='Login']")
        self.btn_registration = page.locator("//button[text()='Registration']")

    def type_login_registration_form(self, user: User) -> None:
        self.input_email.fill(user.username)
        self.input_password.fill(user.password)

    def click_btn_login(self) -> None:
         self.btn_login.click()

    def click_btn_registration(self) -> None:
         self.btn_registration.click()

    def click_btn_login_and_get_alert(self) -> str:
         return self.click_and_get_alert_text(self.btn_login)

    def click_btn_registration_and_get_alert(self) -> str:
        return self.click_and_get_alert_text(self.btn_registration)