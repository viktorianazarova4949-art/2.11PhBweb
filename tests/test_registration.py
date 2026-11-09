import pytest

from models.user import User
from utils.factory import random_user
from pages.login_page import LoginPage
from pages.contacts_page import ContactsPage
from utils.data_reader import wrong_email_password_users

WRONG_FORMAT = "Wrong email or password format"

def test_registration_positive(login_page: LoginPage):
    login_page.type_login_registration_form(random_user())
    login_page.click_btn_registration()
    assert ContactsPage(login_page.page).validate_text_in_no_contact_message(" No Contacts here!")


def test_registration_negative_all_fields_empty(login_page: LoginPage):
    assert WRONG_FORMAT in login_page.click_btn_registration_and_get_alert()

@pytest.mark.parametrize("user", wrong_email_password_users(),
                         ids=lambda user: f"{user.username}|{user.password}")
def test_registration_negative_wrong_email_or_password(login_page: LoginPage, user: User):
    login_page.type_login_registration_form(user)
    assert WRONG_FORMAT in login_page.click_btn_registration_and_get_alert()