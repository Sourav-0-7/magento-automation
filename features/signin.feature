Feature: User Sign-in
  As a registered user
  I want to sign in
  So I can access my account

  Scenario Outline: Successful Sign-in
    Given I am on the Magento homepage
    When I go to the sign-in page
    And I enter sign-in details "<email>", "<password>"
    Then I see the welcome message "Welcome, John Doe!"

    Examples:
      | email                     | password  |
      | john{timestamp}@test.com | Test@123 |

  Scenario Outline: Sign-in with Invalid Password
    Given I am on the Magento homepage
    When I go to the sign-in page
    And I enter sign-in details "<email>", "<password>"
    Then I see the error message "The account sign-in was incorrect"

    Examples:
      | email                     | password   |
      | john{timestamp}@test.com | Wrong@123 |

  Scenario: Sign-in with Empty Fields
    Given I am on the Magento homepage
    When I go to the sign-in page
    And I submit the sign-in form without fields
    Then I see the error message "A login and a password are required."

  Scenario Outline: Sign-in with Non-registered Email
    Given I am on the Magento homepage
    When I go to the sign-in page
    And I enter sign-in details "<email>", "<password>"
    Then I see the error message "The account sign-in was incorrect"

    Examples:
      | email                       | password  |
      | nonexist{timestamp}@test.com | Test@123 |