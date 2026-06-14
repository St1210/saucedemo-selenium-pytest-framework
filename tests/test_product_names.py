from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_product_names(setup):

    driver = setup

    driver.get(
        "https://www.saucedemo.com/"
    )

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(driver)

    products = inventory.get_product_names()

    print(products)

    assert "Sauce Labs Backpack" in products