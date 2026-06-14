from pages.menu_page import MenuPage
from selenium.webdriver.common.by import By


def test_logout(logged_in_user):

    driver = logged_in_user

    MenuPage(driver).logout()

    assert driver.find_element(
        By.ID,
        "login-button"
    ).is_displayed()