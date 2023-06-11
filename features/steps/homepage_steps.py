from behave import *
from features.pages.homepage_page import HomePage


@given("I enter a firstname of '{name}'")
def I_enter_a_firstname(context, name):
    context.homepage = HomePage(context.driver)
    context.homepage.enter_name(name)


@given("I enter an email of '{email}'")
def I_enter_an_email(context, email):
    context.homepage = HomePage(context.driver)
    context.homepage.enter_email(email)


@given("I enter a password of '{password}'")
def I_enter_a_password(context, password):
    context.homepage = HomePage(context.driver)
    context.homepage.enter_password(password)


@given("I select the checkbox")
def I_select_the_checkbox(context):
    context.homepage = HomePage(context.driver)
    context.homepage.check_checkbox()


@given("I select a gender of '{gender}'")
def I_select_a_gender(context, gender):
    context.homepage = HomePage(context.driver)
    context.homepage.enter_gender(gender)


@when("I click the submit button")
def I_click_the_submit_button(context):
    context.homepage = HomePage(context.driver)
    context.homepage.click_submit()


@then("I should see a success message")
def I_should_see_a_success_message(context):
    context.homepage = HomePage(context.driver)
    assert "success" in context.homepage.select_message().text
