from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By

def test_checkout(logged_in_user):

    driver = logged_in_user

    InventoryPage(driver).add_backpack_to_cart()

    cart = CartPage(driver)

    cart.open_cart()

    checkout = CheckoutPage(driver)

    checkout.click_checkout()

    print("STEP 1 URL:", driver.current_url)

    checkout.enter_checkout_info(
    "Sushant",
    "Tawade",
    "400001"
)

    print(
    driver.find_element(By.ID, "first-name")
    .get_attribute("value")
)

    print(
    driver.find_element(By.ID, "last-name")
    .get_attribute("value")
)

    print(
    driver.find_element(By.ID, "postal-code")
    .get_attribute("value")
)

    checkout.click_continue()

    print("AFTER CONTINUE:", driver.current_url)