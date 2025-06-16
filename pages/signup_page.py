from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignupPage(BasePage):
    FIRST_NAME_FIELD = (By.ID, "firstname")
    LAST_NAME_FIELD = (By.ID, "lastname")
    EMAIL_FIELD = (By.ID, "email_address")
    PASSWORD_FIELD = (By.ID, "password")
    CONFIRM_PASSWORD_FIELD = (By.ID, "password-confirmation")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[title='Create an Account']")
    WELCOME_MESSAGE = (By.CSS_SELECTOR, ".logged-in")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".message-error")
    REQUIRED_FIELD_ERRORS = (By.CSS_SELECTOR, ".field-error")

    def fill_signup_form(self, first_name, last_name, email, password, confirm_password):
        if first_name:
            self.send_keys(self.FIRST_NAME_FIELD, first_name)
        if last_name:
            self.send_keys(self.LAST_NAME_FIELD, last_name)
        if email:
            self.send_keys(self.EMAIL_FIELD, email)
        if password:
            self.send_keys(self.PASSWORD_FIELD, password)
        if confirm_password:
            self.send_keys(self.CONFIRM_PASSWORD_FIELD, confirm_password)
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def submit_empty_form(self):
        self.click(self.CREATE_ACCOUNT_BUTTON)

    def get_welcome_message(self):
        return self.get_text(self.WELCOME_MESSAGE)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_required_field_errors(self):
        errors = [elem.text for elem in self.driver.find_elements(*self.REQUIRED_FIELD_ERRORS)]
        return errors