from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_page(setup):

    driver = setup

    driver.get(
        "https://www.saucedemo.com/"
    )

    login = LoginPage(driver)

    login.login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(driver)

    assert inventory.get_product_count() == 6