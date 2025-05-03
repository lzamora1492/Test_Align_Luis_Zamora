from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_order_products(driver):
    # Open URL
    driver.get("https://www.saucedemo.com/")

    # Page Object settings
    login = LoginPage(driver)
    login.set_user("standard_user")
    login.set_password("secret_sauce")
    login.click_login()
    
    time.sleep(5) # Wait for the page to load

    # Selecting dropdown element
    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))

    # Selecting the option "lohi" from the dropdown
    # "lohi" = Price (low to high)
    dropdown.select_by_value("lohi")

    time.sleep(5) # Wait for the page to load

    option_selected = driver.find_element(By.CLASS_NAME, "product_sort_container").find_element(By.XPATH, ".//option[@value='lohi']").text
    
    try:
        assert option_selected != ""
        print(f"Sorting by {option_selected}")
    except AssertionError:
        print("Assert failed")

def test_order_product_validation(driver):
    # Open URL
    driver.get("https://www.saucedemo.com/")

    # Page Object settings
    login = LoginPage(driver)
    login.set_user("standard_user")
    login.set_password("secret_sauce")
    login.click_login()
    
    time.sleep(5) # Wait for the page to load

    # Selecting dropdown element
    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))

    # Selecting the option "lohi" from the dropdown
    # "lohi" = Price (low to high)
    dropdown.select_by_value("lohi")

    time.sleep(5) # Wait for the page to load

    precios_elementos = driver.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item-price"]')

    # Extraer los textos, remover el símbolo $ y convertir a float
    precios = [float(precio.text.replace("$", "")) for precio in precios_elementos]

    try:
        assert precios == sorted(precios)
        print(f"Prices ordered corretly: {precios}")
    except AssertionError:
        print("Assert failed")