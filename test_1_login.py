from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time

def test_login_successful(driver):
    # Open URL
    driver.get("https://www.saucedemo.com/")

    # Page Object settings
    login = LoginPage(driver)
    login.set_user("standard_user")
    login.set_password("secret_sauce")
    login.click_login()

    # Wait for the page to load
    time.sleep(2) # Wait for the page to load

    # Check if the URL is correct after login
    
    try:
        assert "www.saucedemo.com/inventory.html" in driver.current_url
        print("Succesful Login.")
    except AssertionError:
        print("Assert failed")
    
    
def test_login_fail(driver):
    # Open URL
    driver.get("https://www.saucedemo.com/")

    # Page Object settings
    login = LoginPage(driver)
    login.set_user("standard_user")
    login.set_password("secret_sauc")
    login.click_login()

    # Wait for the page to load
    time.sleep(2) # Wait for the page to load

    # Check if the URL is incorrect after login
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    texto = error_message.text
    
    try:
        assert "Epic sadface: Username and password do not match any user in this service" in texto
        print(f"Login failed. Wrong credentials. Error message: {texto}")
    except AssertionError:
        print("Assert failed")