Feature: User Signup on Magento Website
  As a new user
  I want to create an account
  So that I can access personalized features

  Scenario Outline: Successful Signup
    Given I am on the Magento homepage
    When I navigate to the signup page
    And I enter valid signup details "<first_name>", "<last_name>", "<email>", "<password>", "<confirm_password>"
    Then I should see the welcome message "Welcome, <first_name> <last_name>!"

    Examples:
      | first_name | last_name | email                       | password  | confirm_password |
      | John       | Doe       | john.doe{timestamp}@test.com | Test@123 | Test@123         |

  Scenario Outline: Signup with Existing Email
    Given I am on the Magento homepage
    When I navigate to the signup page
    And I enter signup details "<first_name>", "<last_name>", "<email>", "<password>", "<confirm_password>"
    Then I should see the error message "There is already an account with this email address."

    Examples:
      | first_name | last_name | email                       | password  | confirm_password |
      | Jane       | Smith     | john.doe{timestamp}@test.com | Test@123 | Test@123         |

  Scenario: Signup with Empty Fields
    Given I am on the Magento homepage
    When I navigate to the signup page
    And I submit the signup form without filling fields
    Then I should see required field errors

  Scenario Outline: Signup with Invalid Email
    Given I am on the Magento homepage
    When I navigate to the signup page
    And I enter signup details "<first_name>", "<last_name>", "<email>", "<password>", "<confirm_password>"
    Then I should see the error message "Please enter a valid email address (ex: johndoe@domain.com)."

    Examples:
      | first_name | last_name | email         | password  | confirm_password |
      | John       | Doe       | invalid.email | Test@123 | Test@123         |

  Scenario Outline: Signup with Mismatched Passwords
    Given I am on the Magento homepage
    When I navigate to the signup page
    And I enter signup details "<first_name>", "<last_name>", "<email>", "<password>", "<confirm_password>"
    Then I should see the error message "Please enter the same value again."

    Examples:
      | first_name | last_name | email                       | password  | confirm_password |
      | John       | Doe       | john.doe{timestamp}@test.com | Test@123 | Test@456         |

  Scenario Outline: Signup with Weak Password
    Given I am on the Magento homepage
    When I navigate to the signup page
    And I enter signup details "<first_name>", "<last_name>", "<email>", "<password>", "<confirm_password>"
    Then I should see the error message "Minimum length of this field must be equal or greater than 8 symbols"

    Examples:
      | first_name | last_name | email                       | password | confirm_password |
      | John       | Doe       | john.doe{timestamp}@test.com | abc      | abc              |