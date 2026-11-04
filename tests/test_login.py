import pytest

from models.user import User
from pages.login_page import LoginPage
from pages.contacts_page import ContactsPage
from utils.soft_assert import SoftAssert
from utils.config_reader import get_property


def test_login_positive(login_page: LoginPage, base_user: User):
    login_page.type_login_registration_form(base_user)
    login_page.click_btn_login()
    contacts_page = ContactsPage(login_page.page)
    soft = SoftAssert()
    soft.assert_true(contacts_page.is_link_add_present(), "validate  link add present")
    soft.assert_true(contacts_page.is_url_contains("contacts"), "validate url")
    soft.assert_all()

def test_login_negative_all_fields_empty(login_page: LoginPage):
    assert login_page.click_btn_login_and_get_alert() == "Wrong email or password"

@pytest.mark.parametrize("username,password",
     [
         pytest.param("",get_property("password") , id="empty email"),
         pytest.param(get_property("email"),"", id="empty password"),
         pytest.param(f"s{get_property("email")}",get_property("password") , id="wrong email"),
         pytest.param(get_property("email"),f"{get_property("password")}!" , id="wrong password"),
     ],
     )
def test_login_negative(login_page: LoginPage, username:str, password:str):
    login_page.type_login_registration_form(User(username=username, password=password))
    assert login_page.click_btn_login_and_get_alert() == "Wrong email or password"

