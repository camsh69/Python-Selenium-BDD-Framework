from behave import *
from features.pages.home_page import HomePage


@given("I enter a firstname of '{name}'")
def I_enter_a_firstname(context, name):
    context.homepage = HomePage(context.driver)
    context.homepage.enterName(name)


@given("I enter an email of '{email}'")
def I_enter_an_email(context, email):
    context.homepage = HomePage(context.driver)
    context.homepage.enterEmail(email)


@given("I enter a password of '{password}'")
def I_enter_a_password(context, password):
    context.homepage = HomePage(context.driver)
    context.homepage.enterPassword(password)


@given("I select the checkbox")
def I_select_the_checkbox(context):
    context.homepage = HomePage(context.driver)
    context.homepage.checkCheckBox()


@given("I select a gender of '{gender}'")
def I_select_a_gender(context, gender):
    context.homepage = HomePage(context.driver)
    context.homepage.enterGender(gender)


@when("I click the submit button")
def I_click_the_submit_button(context):
    context.homepage = HomePage(context.driver)
    context.homepage.clickSubmit()


@then("I should see a success message")
def I_should_see_a_success_message(context):
    context.homepage = HomePage(context.driver)
    assert "success" in context.homepage.selectMessage().text
