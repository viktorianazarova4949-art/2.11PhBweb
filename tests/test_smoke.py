import pytest
from playwright.sync_api import Page,expect           # Page — «руки»: навигация, клики, ввод.
                                                        #expect — «глаза»: проверки с умным ожиданием.
                                                        #sync_api — синхронный стиль (команды выполняются по очереди), проще для новичков; есть и async_api для асинхронного кода.

def test_open_home(page: Page):
    page.goto("https://telranedu.web.app/home")
    expect(page.locator("//a[text()='LOGIN']")).to_be_visible()