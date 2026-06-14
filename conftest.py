import pytest
from utilities.driver_factory import DriverFactory
from pages.login_page import LoginPage


@pytest.fixture
def setup():

    driver = DriverFactory.get_driver()

    yield driver

    driver.quit()


@pytest.fixture
def logged_in_user(setup):

    driver = setup

    driver.get("https://www.saucedemo.com/")

    LoginPage(driver).login(
        "standard_user",
        "secret_sauce"
    )

    return driver