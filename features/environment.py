from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.signin_page import SignInPage
from utilities.logger import setup_logger
from utilities.config import get_config
import logging
import time

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.base_url = get_config()['base_url']
    context.logger = setup_logger()
    context.logger.info(f"Starting scenario: {scenario.name}")
    context.home_page = HomePage(context.driver)
    context.signup_page = SignupPage(context.driver)
    context.signin_page = SignInPage(context.driver)
    context.timestamp = str(int(time.time()))  # For unique email

def after_scenario(context, scenario):
    context.logger.info(f"Ending scenario: {scenario.name}")
    context.driver.quit()