# SauceDemo Selenium PyTest Framework

## Overview

This project is an end-to-end test automation framework developed using **Python**, **PyTest**, **Selenium WebDriver**, and the **Page Object Model (POM)** design pattern.

The framework automates key user workflows of the SauceDemo e-commerce application and demonstrates best practices for building scalable and maintainable UI automation frameworks.

---

## Tech Stack

* Python 3.x
* Selenium WebDriver
* PyTest
* Page Object Model (POM)
* WebDriver Manager
* Git & GitHub

---

## Project Structure

```text
saucedemo/
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── menu_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_product_names.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_logout.py
│
├── utilities/
│   └── driver_factory.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

## Automated Test Scenarios

### Login Module

* Valid user login
* Login verification

### Inventory Module

* Verify inventory page loads successfully
* Validate product count
* Validate product names

### Cart Module

* Add product to cart
* Verify product details in cart
* Verify product price
* Remove product from cart

### Checkout Module

* Complete checkout flow
* Validate checkout overview page
* Verify successful order placement

### Logout Module

* Logout from application
* Verify user is redirected to login page

---

## Design Pattern Used

### Page Object Model (POM)

The framework follows the Page Object Model design pattern where:

* Locators are maintained separately from test logic.
* Each page has its own Page Class.
* Tests remain clean and reusable.
* Maintenance becomes easier as the application grows.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/St1210/saucedemo-selenium-pytest-framework.git
```

Navigate to the project directory:

```bash
cd saucedemo-selenium-pytest-framework
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Execute Tests

Run all tests:

```bash
pytest -v
```

Run a specific test:

```bash
pytest tests/test_login.py -v
```

---

## Framework Highlights

* PyTest Fixtures
* Reusable Page Objects
* Explicit Waits
* Driver Factory Pattern
* Modular Test Design
* Scalable Framework Structure

---

## Test Results

Current Automation Coverage:

* Login
* Inventory Validation
* Product Validation
* Add To Cart
* Cart Validation
* Checkout Flow
* Logout Flow

All implemented test cases are passing successfully.

---

## Future Enhancements

* Base Page Implementation
* Screenshot Capture on Failure
* PyTest HTML Reports
* Allure Reporting
* Data-Driven Testing
* Excel Integration
* Jenkins CI/CD Integration
* GitHub Actions Pipeline
* Parallel Execution

---

