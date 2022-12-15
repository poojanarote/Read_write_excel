from behave import *
from selenium import webdriver


@given('launch google chrome')
def step_impl(context):
    print(1)

@when('open the site')
def step_impl(context):
    print(1)

@then('user is on the homepage')
def step_impl(context):
    print(1)