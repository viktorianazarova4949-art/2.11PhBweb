from pages import add_contact_page
from pages.contacts_page import ContactsPage
from pages.add_contact_page import AddContactPage
from utils.factory import random_contact
import pytest

@pytest.fixture
def add_page(contacts_page: ContactsPage) -> AddContactPage:
    contacts_page.click_link_add()
    return AddContactPage(contacts_page.page)

def test_add_new_contact_positive(contacts_page: ContactsPage, add_page: AddContactPage):
    add_page.type_add_contact_form(random_contact())
    add_page.click_btn_save()