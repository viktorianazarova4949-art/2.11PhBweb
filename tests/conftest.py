import pytest
from playwright.async_api import Page
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page)->LoginPage:
    HomePage(page).open().click_link_login()
    return LoginPage(page)