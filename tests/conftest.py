import pytest
from playwright.sync_api import Page

from models.user import User
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config_reader import get_property



@pytest.fixture
def login_page(page: Page)->LoginPage:
    HomePage(page).open().click_link_login()
    return LoginPage(page)

@pytest.fixture
def base_user()->User:
    return User(username=get_property("email"), password=get_property("password"))