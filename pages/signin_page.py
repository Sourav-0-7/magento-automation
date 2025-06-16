from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignInPage(BasePage):
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "pass")
    SIGN_IN_BUTTON = (By.ID, "send2")
    WELCOME_MESSAGE = (By.CSS_SELECTOR, ".logged-in")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".message-error")

    def fill_signin_form(self, email, password):
        if email:
            self.send_keys(self.EMAIL_FIELD, email)
        if password:
            self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.SIGN_IN_BUTTON)

    def submit_empty_form(self):
        self.click(self.SIGN_IN_BUTTON)

    def get_welcome_message(self):
        return self.get_text(self.WELCOME_MESSAGE)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)