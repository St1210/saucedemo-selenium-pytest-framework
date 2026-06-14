import pytest
from pages.login_page import LoginPage


# =====================
# Positive Tests
# =====================

def test_valid_login(setup):

    login = LoginPage(setup)

    login.open()

    login.login(
        "standard_user",
        "secret_sauce"
    )

    assert login.is_login_successful()


def test_logout(setup):

    login = LoginPage(setup)

    login.open()

    login.login(
        "standard_user",
        "secret_sauce"
    )

    login.logout()

    assert "saucedemo.com" in setup.current_url


# =====================
# Negative Tests
# =====================

@pytest.mark.parametrize(
    "username,password,error_text",
    [
        (
            "invalid_user",
            "secret_sauce",
            "Username and password do not match"
        ),
        (
            "standard_user",
            "wrong_password",
            "Username and password do not match"
        ),
        (
            "",
            "secret_sauce",
            "Username is required"
        ),
        (
            "standard_user",
            "",
            "Password is required"
        ),
        (
            "",
            "",
            "Username is required"
        )
    ]
)
def test_invalid_login(
        setup,
        username,
        password,
        error_text):

    login = LoginPage(setup)

    login.open()

    login.login(
        username,
        password
    )

    assert error_text in login.get_error_message()


# =====================
# SauceDemo Users
# =====================

def test_locked_user(setup):

    login = LoginPage(setup)

    login.open()

    login.login(
        "locked_out_user",
        "secret_sauce"
    )

    assert "locked out" in \
           login.get_error_message().lower()


def test_problem_user_login(setup):

    login = LoginPage(setup)

    login.open()

    login.login(
        "problem_user",
        "secret_sauce"
    )

    assert login.is_login_successful()


# =====================
# Security / Edge Cases
# =====================

@pytest.mark.parametrize(
    "username,password",
    [
        (
            "' OR '1'='1",
            "secret_sauce"
        ),
        (
            "<script>alert('xss')</script>",
            "secret_sauce"
        ),
        (
            "  standard_user",
            "secret_sauce"
        ),
        (
            "standard_user  ",
            "secret_sauce"
        )
    ]
)
def test_invalid_special_inputs(
        setup,
        username,
        password):

    login = LoginPage(setup)

    login.open()

    login.login(
        username,
        password
    )

    assert login.get_error_message() is not None