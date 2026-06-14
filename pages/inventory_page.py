from selenium.webdriver.common.by import By

class InventoryPage:

    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")

    def __init__(self, driver):
        self.driver = driver

    def get_product_count(self):
        return len(
            self.driver.find_elements(*self.PRODUCTS)
        )

    def get_product_names(self):
        products = self.driver.find_elements(
            *self.PRODUCT_NAMES
        )

        return [p.text for p in products]

    def add_backpack_to_cart(self):
        self.driver.find_element(
            *self.ADD_TO_CART
        ).click()