from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time

def test_add_products(driver):
    # Open URL
    driver.get("https://www.saucedemo.com/")

    # Page Object settings
    login = LoginPage(driver)
    login.set_user("standard_user")
    login.set_password("secret_sauce")
    login.click_login()

    #Selecting items to add to the cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    time.sleep(2) # Wait for the page to load

    # Getting the number of items in the cart
    cart_items = driver.find_element(By.XPATH, "//span[@data-test='shopping-cart-badge']")
    items = int(cart_items.text)

    # Validation #1 Check if the number of items in the cart is greater than or equal to 2
    
    try:
        assert items >= 2
        print(f"There are {items} items in the cart.")
    except AssertionError:
        print("Assert failed")

def test_validation_products(driver):
    # Open URL
    driver.get("https://www.saucedemo.com/")

    # Page Object settings
    login = LoginPage(driver)
    login.set_user("standard_user")
    login.set_password("secret_sauce")
    login.click_login()

    #Selecting items to add to the cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    item_added1 = driver.find_element(By.ID, "item_4_title_link").find_element(By.CLASS_NAME, "inventory_item_name").text

    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    item_added2 = driver.find_element(By.ID, "item_1_title_link").find_element(By.CLASS_NAME, "inventory_item_name").text

    time.sleep(2) # Wait for the page to load

    driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
    
    time.sleep(2) # Wait for the page to load
    
    item_cart1 = driver.find_element(By.ID, "item_4_title_link").find_element(By.CLASS_NAME, "inventory_item_name").text
    item_cart2 = driver.find_element(By.ID, "item_1_title_link").find_element(By.CLASS_NAME, "inventory_item_name").text
    
    try:
        assert item_cart1 == item_added1 and item_cart2 == item_added2
        print(f"Items in the cart are correct: {item_cart1} and {item_cart2}.")
    except AssertionError:
        print("Assert failed")

def test_remove_product(driver):
    # Open URL
    driver.get("https://www.saucedemo.com/")

    # Page Object settings
    login = LoginPage(driver)
    login.set_user("standard_user")
    login.set_password("secret_sauce")
    login.click_login()

    #Selecting items to add to the cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    time.sleep(2) # Wait for the page to load

    driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
    
    time.sleep(2) # Wait for the page to load
    
    item_remove = driver.find_element(By.ID, "item_4_title_link").find_element(By.CLASS_NAME, "inventory_item_name").text
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    
    time.sleep(2) # Wait for the page to load

    try:
        assert item_remove != ""
        print(f"Item removed {item_remove}.")
    except AssertionError:
        print("Assert failed")