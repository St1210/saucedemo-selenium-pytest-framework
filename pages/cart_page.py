from selenium.webdriver.common.by import By

class CartPage:

    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    PRODUCT_NAME = (
        By.CLASS_NAME,
        "inventory_item_name"
    )

    PRODUCT_PRICE = (
        By.CLASS_NAME,
        "inventory_item_price"
    )

    REMOVE_BUTTON = (
        By.ID,
        "remove-sauce-labs-backpack"
    )

    TOTAL = (
    By.CLASS_NAME,
    "summary_total_label"
    )

    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        self.driver.find_element(
            *self.CART_ICON
        ).click()

    def get_product_name(self):
        return self.driver.find_element(
            *self.PRODUCT_NAME
        ).text

    def get_product_price(self):
        return self.driver.find_element(
            *self.PRODUCT_PRICE
        ).text

    def remove_product(self):
        self.driver.find_element(
            *self.REMOVE_BUTTON
        ).click()

    def get_total(self):
        return self.driver.find_element(
        *self.TOTAL
    ).text

        assert "Total" in checkout.get_total()