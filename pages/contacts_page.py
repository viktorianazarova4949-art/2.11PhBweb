from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class ContactsPage(BasePage):
    def __init__(self, page:Page) -> None:
        super().__init__(page)
        self.link_add = page.locator("a[href='/add']")
        self.no_contact_message = page.locator("h1", has_text=" No Contacts here!")
        self.list_contacts = page.locator(".contact-item_card__2SOIM")
        self.last_contact = self.list_contacts.last.locator("h3")


    def is_link_add_present(self) -> bool:
        return self.is_element_visible(self.link_add)

    def validate_text_in_no_contact_message(self, text: str) -> bool:
        return self.is_text_in_element_present(self.no_contact_message, text)

    def validate_text_in_last_contacts(self, text: str) -> bool:
        return self.is_text_in_element_present(self.last_contact, text)

    def click_link_add(self):
        self.link_add.click()

    def count_contacts(self) -> int:
        return self.list_contacts.count()

    def wait_count_of_contacts(self, expected: int, timeout: int = 10_000) -> int:
        """Ждём, пока число контактов станет равным expected (или истечёт таймаут)."""
        try:
            expect(self.list_contacts).to_have_count(expected, timeout=timeout)
        except AssertionError:
            pass
        return self.count_contacts()


    def get_text_from_last_contact(self) -> str:
        return self.last_contact.inner_text()