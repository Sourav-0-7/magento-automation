from behave import when, then
from utilities.config import get_config

@when('I navigate to the signup page')
def step_impl(context):
    context.home_page.navigate_to_signup()
    context.logger.info("Navigated to signup page")

@when('I enter valid signup details "{first_name}", "{last_name}", "{email}", "{password}", "{confirm_password}"')
def step_impl(context, first_name, last_name, email, password, confirm_password):
    email = email.replace("{timestamp}", context.timestamp)
    context.signup_email = email  # Store for sign-in
    context.signup_page.fill_signup_form(first_name, last_name, email, password, confirm_password)

@when('I enter signup details "{first_name}", "{last_name}", "{email}", "{password}", "{confirm_password}"')
def step_impl(context, first_name, last_name, email, password, confirm_password):
    email = email.replace("{timestamp}", context.timestamp)
    context.signup_page.fill_signup_form(first_name, last_name, email, password, confirm_password)

@when('I submit the signup form without filling fields')
def step_impl(context):
    context.signup_page.submit_empty_form()

@then('I should see the welcome message "{expected_message}"')
def step_impl(context, expected_message):
    actual_message = context.signup_page.get_welcome_message()
    assert expected_message in actual_message, f"Expected '{expected_message}', got '{actual_message}'"
    context.logger.info(f"Verified welcome message")

@then('I should see the error message "{expected_message}"')
def step_impl(context, expected_message):
    actual_message = context.signup_page.get_error_message()
    assert expected_message in actual_message, f"Expected '{expected_message}', got '{actual_message}'"
    context.logger.info(f"Verified error message")

@then('I should see required field errors')
def step_impl(context):
    errors = context.signup_page.get_required_field_errors()
    assert len(errors) > 0, "No required field errors found"
    for error in errors:
        assert "This is a required field" in error, f"Expected 'This is a required field', got '{error}'"
    context.logger.info("Verified required field errors")