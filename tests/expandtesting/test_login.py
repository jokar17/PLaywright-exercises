from playwright.sync_api import Page, expect

def test_login_valido(page: Page):
    page.goto("https://practice.expandtesting.com/login")
    page.locator("#username").fill("practice")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("#submit-login").click()

    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")