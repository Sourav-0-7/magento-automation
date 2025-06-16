from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    CREATE_ACCOUNT_LINK = (By.LINK_TEXT, "Create an Account")
    SIGN_IN_LINK = (By.LINK_TEXT, "Sign In")

    def navigate_to_signup(self):
        self.click(self.CREATE_ACCOUNT_LINK)

    def navigate_to_signin(self):
        self.click(self.SIGN_IN_LINK)