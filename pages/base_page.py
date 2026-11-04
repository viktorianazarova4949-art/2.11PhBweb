from playwright.sync_api import Page, expect, Locator, TimeoutError as PlaywrightTimeoutError
import re

DEFAULT_TIMEOUT = 5_000

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def is_url_contains(self, text: str, timeout:int = DEFAULT_TIMEOUT) -> bool:
        try:
            expect(self.page).to_have_url(re.compile(re.escape(text)), timeout=timeout)
            return True
        except AssertionError:
            print(f"AssertionError: {text}")
            return False

    def is_element_visible(self, locator: Locator, timeout:int = DEFAULT_TIMEOUT) -> bool:
        try:
            locator.wait_for(state="visible", timeout=timeout)
            return True
        except PlaywrightTimeoutError:
            return False

    def is_text_in_element_present(self, locator: Locator, text: str, timeout:int = DEFAULT_TIMEOUT) -> bool:
        try:
            expect(locator).to_contain_text(text, timeout=timeout)
            return True
        except AssertionError:
            print(f"AssertionError: {text}")
            return False

    def click_and_get_alert_text(self, locator: Locator, timeout:int = DEFAULT_TIMEOUT) -> str:
        with self.page.expect_event("dialog", timeout=timeout) as dialog_info:
            locator.click()
            dialog = dialog_info.value
            text = dialog.message
            dialog.accept()
            return text