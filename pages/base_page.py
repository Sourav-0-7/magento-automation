from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import setup_logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = setup_logger()
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.logger.info(f"Found element: {locator}")
            return element
        except Exception as e:
            self.logger.error(f"Element not found: {locator}. Error: {e}")
            raise

    def click(self, locator):
        try:
            self.find_element(locator).click()
            self.logger.info(f"Clicked element: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to click: {locator}. Error: {e}")
            raise

    def send_keys(self, locator, text):
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Sent keys '{text}' to: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to send keys to: {locator}. Error: {e}")
            raise

    def get_text(self, locator):
        try:
            text = self.find_element(locator).text
            self.logger.info(f"Got text '{text}' from: {locator}")
            return text
        except Exception as e:
            self.logger.error(f"Failed to get text from: {locator}. Error: {e}")
            raise