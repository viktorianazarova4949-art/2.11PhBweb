from pages.base_page import BasePage
from  playwright.sync_api import Page
from models.contact import Contact


class AddContactPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.input_name = page.get_by_placeholder("Name")
        self.input_last_name = page.get_by_placeholder("LastName")
        self.input_phone = page.get_by_placeholder("Phone")
        self.input_email = page.get_by_placeholder("email")
        self.input_address = page.get_by_placeholder("Address")
        self.input_description = page.get_by_placeholder("description")
        self.btn_save = page.locator("//b[text()='Save']")

    def type_add_contact_form(self, contact: Contact) -> None:
        self.input_name.fill(contact.name)
        self.input_last_name.fill(contact.lastName)
        self.input_phone.fill(contact.phone)
        self.input_email.fill(contact.email)
        self.input_address.fill(contact.address)
        self.input_description.fill(contact.description)

    def click_btn_save(self):
        self.btn_save.click()