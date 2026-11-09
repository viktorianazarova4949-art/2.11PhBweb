import time

from pages.contacts_page import ContactsPage
from pages.add_contact_page import AddContactPage
from utils.factory import random_contact
import pytest



def test_add_new_contact_positive(contacts_page: ContactsPage):
    count_contacts_before = contacts_page.count_contacts()
    print(f"\nContacts before adding: {count_contacts_before}")

    contacts_page.click_link_add()
    add_page = AddContactPage(contacts_page.page)
    add_page.type_add_contact_form(random_contact())
    add_page.click_btn_save()

    exp = count_contacts_before + 1
    count_after = contacts_page.count_contacts()
    print(f"Contacts after adding: {count_after} (expected {exp})")

    assert count_after == exp

def test_add_new_contact_positive_check_last_contact(contacts_page: ContactsPage):
    contact = random_contact()
    count_contacts_before = contacts_page.count_contacts()
    contacts_page.click_link_add()
    add_page = AddContactPage(contacts_page.page)
    add_page.type_add_contact_form(contact)
    add_page.click_btn_save()
    contacts_page.wait_count_of_contacts(count_contacts_before + 1)

    text = contacts_page.get_text_from_last_contact()
    assert contact.phone == text

@pytest.fixture
def added_contact(contacts_page: ContactsPage):
    count_contacts_before = contacts_page.count_contacts()
    contacts_page.click_link_add()
    add_page = AddContactPage(contacts_page.page)

    contact = random_contact()
    add_page.type_add_contact_form(contact)
    add_page.click_btn_save()
    return contact, count_contacts_before


