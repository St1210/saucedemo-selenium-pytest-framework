from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.CHECKOUT_BUTTON
            )
        ).click()

    def enter_checkout_info(
            self,
            first_name,
            last_name,
            zip_code):

        self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        ).send_keys(first_name)

        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys(last_name)

        self.driver.find_element(
            *self.ZIP_CODE
        ).send_keys(zip_code)

    def click_continue(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_BUTTON
            )
        ).click()

    def click_finish(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.FINISH_BUTTON
            )
        ).click()

    def get_success_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.SUCCESS_MESSAGE
            )
        ).text