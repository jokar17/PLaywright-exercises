import pytest
from playwright.sync_api import Page, expect

# using mark.parametrize
@pytest.mark.parametrize("username,password,expected,url",[
    ("practice","SuperSecretPassword!","You logged into a secure area!","/secure"),
    ("vero","SuperSecretPassword!", "Your username is invalid!", "/login"),
    ("practice","wrongPassword", "Your password is invalid!", "/login")

], ids=["login_valido", "username_invalido", "password_invalida"])


def test_login_validation(page: Page, username, password, expected, url):
    page.goto("/login")
    page.locator("#username").fill(username)
    page.locator("#password").fill(password)
    page.locator("#submit-login").click()

    expect(page.locator("#flash")).to_contain_text(expected)
    expect(page).to_have_url(url)
    

    
