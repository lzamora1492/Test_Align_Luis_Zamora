from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.NAME, "user-name")
        self.password = (By.NAME, "password")
        self.login_btn = (By.NAME, "login-button")

    def set_user(self, user):
        self.driver.find_element(*self.username).send_keys(user)

    def set_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()
