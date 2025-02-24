import re
import time

from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    time.sleep(5)
    page.get_by_placeholder("What needs to be done?").press("CapsLock")
    page.get_by_placeholder("What needs to be done?").fill("AA")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    time.sleep(5)
    page.get_by_placeholder("What needs to be done?").fill("BB")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("CC")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").press("CapsLock")
    page.get_by_text("CC").click()
    page.locator("li").filter(has_text="CC").get_by_label("Toggle Todo").check()
    page.get_by_role("link", name="Active").click()
    page.get_by_role("button", name="Clear completed").click()
    page.get_by_role("link", name="All").click()
