import pytest
from utils.factory import random_user
from pages.login_page import LoginPage
from pages.contacts_page import ContactsPage

def test_registration_positive(login_page: LoginPage):
    login_page.type_login_registration_form(random_user())
    login_page.click_btn_registration()
    assert ContactsPage(login_page.page).validate_text_in_no_contact_message(" No Contacts here!")
