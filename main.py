from playwright.sync_api import Playwright, sync_playwright, expect
import time 


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    page.get_by_role("button", name="Log in").click()
    page.wait_for_load_state("networkidle")
    page.get_by_role("link", name=" Promotions ").click()
    page.get_by_role("link", name=" Discounts").click()
    page.get_by_role("link", name=" Discounts").click()
    page.get_by_role("link", name=" Add new").click()
    page.get_by_label("Name").click()
    page.get_by_label("Name").fill("250FF")
    page.get_by_label("Use percentage").check()
    page.get_by_role("spinbutton", name="0.0000").click()
    page.get_by_label("Discount percentage").fill("25")
    # page.get_by_text("Is active Name * Discount").click()
    page.get_by_label("Requires coupon code").check()
    page.get_by_label("Coupon code", exact=True).click()
    page.get_by_label("Coupon code", exact=True).fill("250FF")
    page.locator("#pnlDiscountPercentage div").nth(3).click()
    page.locator("section").click()
    page.locator(".k-picker-wrap > .k-select > span > .k-icon").first.click()
    page.get_by_title("Friday, March 1,").click()
    page.locator("div:nth-child(12) > .col-md-9 > .k-widget > .k-picker-wrap > .k-select > span > .k-icon").first.click()
    page.get_by_role("link", name="31").click()
    page.get_by_role("button", name=" Save", exact=True).click()
    
    time.sleep(5)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
