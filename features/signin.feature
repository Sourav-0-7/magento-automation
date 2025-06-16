Feature: User Sign-in on Magento Website
  As a registered user
  I want to sign in to my account
  So that I can access my account features

  Scenario Outline: Successful Sign-in
    Given I am on the Magento homepage
    When I navigate to the sign-in page
    And I enter valid sign-in details "<email>", "<password>"
    Then I should see the welcome message "Welcome, John Doe!"

    Examples:
      | email                       | password  |
      | john.doe{timestamp}@test.com | Test@123 |

  Scenario Outline: Sign-in with Invalid Password
    Given I am on the Magento homepage
    When I navigate to the sign-in page
    And I enter sign-in details "<email>", "<password>"
    Then I should see the error message "The account sign-in was incorrect or your account is disabled temporarily."

    Examples:
      | email                       | password   |
      | john.doe{timestamp}@test.com | Wrong@123 |

  Scenario: Sign-in with Empty Fields
    Given I am on the Magento homepage
    When I navigate to the sign-in page
    And I submit the sign-in form without filling fields
    Then I should see the error message "A login and a password are required."

  Scenario Outline: Sign-in with Non-registered Email
    Given I am on the Magento homepage
    When I navigate to the sign-in page
    And I enter sign-in details "<email>", "<password>"
    Then I should see the error message "The account sign-in was incorrect or your account is disabled temporarily."

    Examples:
      | email                      | password  |
      | nonexist{timestamp}@test.com | Test@123 |