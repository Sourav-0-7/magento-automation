from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.signin_page import SignInPage
import time

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.home_page = HomePage(context.driver)
    context.signup_page = SignupPage(context.driver)
    context.signin_page = SignInPage(context.driver)
    context.timestamp = str(int(time.time()))

def after_scenario(context, scenario):
    context.driver.quit()