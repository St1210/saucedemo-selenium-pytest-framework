from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_verify_product_in_cart(setup):

    driver = setup

    driver.get(
        "https://www.saucedemo.com/"
    )

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(driver)

    inventory.add_backpack_to_cart()

    cart = CartPage(driver)

    cart.open_cart()

    assert (
        cart.get_product_name()
        == "Sauce Labs Backpack"
    )

def test_verify_product_price(setup):

    driver = setup

    driver.get(
        "https://www.saucedemo.com/"
    )

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    InventoryPage(driver).add_backpack_to_cart()

    cart = CartPage(driver)

    cart.open_cart()

    assert cart.get_product_price() == "$29.99"

def test_remove_product(setup):

    driver = setup

    driver.get(
        "https://www.saucedemo.com/"
    )

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    InventoryPage(driver).add_backpack_to_cart()

    cart = CartPage(driver)

    cart.open_cart()

    cart.remove_product()

    assert "cart.html" in driver.current_url