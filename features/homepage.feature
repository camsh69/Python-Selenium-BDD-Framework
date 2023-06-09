Feature: Homepage Login

    As a user
    I want to enter my credentials
    So I can Login

    Scenario: Login to Homepage with username, email and password
        Given I enter a firstname of 'Joe'
        And I enter an email of 'dummy@email.com'
        And I enter a password of 'password'
        And I select the checkbox
        And I select a gender of 'Male'
        When I click the submit button
        Then I should see a success message

    Scenario Outline: Login to Homepage with username, email and password
        Given I enter a firstname of '<first_name>'
        And I enter an email of '<email>'
        And I enter a password of '<password>'
        And I select the checkbox
        And I select a gender of '<gender>'
        When I click the submit button
        Then I should see a success message

        Examples:
            | first_name | email           | password | gender |
            | Joe        | dummy@email.com | password | Male   |
            | Sue        | dummy@email.com | password | Female |
