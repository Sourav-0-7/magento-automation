from behave import when, then
from utilities.config import get_config

@when('I navigate to the sign-in page')
def step_impl(context):
    context.home_page.navigate_to_signin()
    context.logger.info("Navigated to sign-in page")

@when('I enter valid sign-in details "{email}", "{password}"')
def step_impl(context, email, password):
    email = email.replace("{timestamp}", context.timestamp)
    context.signin_page.fill_signin_form(email, password)

@when('I enter sign-in details "{email}", "{password}"')
def step_impl(context, email, password):
    email = email.replace("{timestamp}", context.timestamp)
    context.signin_page.fill_signin_form(email, password)

@when('I submit the sign-in form without filling fields')
def step_impl(context):
    context.signin_page.submit_empty_form()

@then('I should see the welcome message "{expected_message}"')
def step_impl(context, expected_message):
    actual_message = context.signin_page.get_welcome_message()
    assert expected_message in actual_message, f"Expected '{expected_message}', got '{actual_message}'"
    context.logger.info(f"Verified welcome message")

@then('I should see the error message "{expected_message}"')
def step_impl(context, expected_message):
    actual_message = context.signin_page.get_error_message()
    assert expected_message in actual_message, f"Expected '{expected_message}', got '{actual_message}'"
    context.logger.info(f"Verified error message")