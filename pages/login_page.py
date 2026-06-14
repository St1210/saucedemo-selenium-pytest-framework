from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "https://www.saucedemo.com/"

    # Login Page Locators
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    # Inventory Page Locators
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver

    # -------------------------
    # Navigation Methods
    # -------------------------

    def open(self):
        self.driver.get(self.URL)

    # -------------------------
    # Login Methods
    # -------------------------

    def enter_username(self, username):
        self.driver.find_element(
            *self.USERNAME
        ).clear()

        self.driver.find_element(
            *self.USERNAME
        ).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(
            *self.PASSWORD
        ).clear()

        self.driver.find_element(
            *self.PASSWORD
        ).send_keys(password)

    def click_login(self):
        self.driver.find_element(
            *self.LOGIN_BUTTON
        ).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # -------------------------
    # Logout Method
    # -------------------------

    def logout(self):

        self.driver.find_element(
            *self.MENU_BUTTON
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                self.LOGOUT_LINK
            )
        )

        self.driver.find_element(
            *self.LOGOUT_LINK
        ).click()

    # -------------------------
    # Validation Methods
    # -------------------------

    def get_error_message(self):
        try:
            error = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(
                    self.ERROR_MESSAGE
                )
            )
            return error.text

        except Exception:
            return None

    def is_login_successful(self):
        return "inventory" in self.driver.current_url

    # -------------------------
    # Utility Methods
    # -------------------------

    def clear_username(self):
        self.driver.find_element(
            *self.USERNAME
        ).clear()

    def clear_password(self):
        self.driver.find_element(
            *self.PASSWORD
        ).clear()

    def clear_all(self):
        self.clear_username()
        self.clear_password()