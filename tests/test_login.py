from pages.login_page import LoginPage

def test_valid_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url
