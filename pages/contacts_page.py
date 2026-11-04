from pages.base_page import BasePage
from playwright.sync_api import Page


class ContactsPage(BasePage):
    def __init__(self, page:Page) -> None:
        super().__init__(page)
        self.link_add = page.locator("a[href='/add']")
        self.no_contact_message = page.locator("h1", has_text=" No Contacts here!")

    def is_link_add_present(self) -> bool:
        return self.is_element_visible(self.link_add)

    def validate_text_in_no_contact_message(self, text: str) -> bool:
        return self.is_text_in_element_present(self.no_contact_message, text)
