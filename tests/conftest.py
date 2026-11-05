import pytest
from playwright.sync_api import Page

from models.user import User
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.contacts_page import ContactsPage
from utils.config_reader import get_property


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    HomePage(page).open().click_link_login()
    return LoginPage(page)

@pytest.fixture
def contacts_page(login_page:LoginPage, base_user: User) -> ContactsPage:
    login_page.type_login_registration_form(base_user)
    login_page.click_btn_login()
    return ContactsPage(login_page.page)


@pytest.fixture
def base_user() -> User:
    return User(username=get_property("email"), password=get_property("password"))