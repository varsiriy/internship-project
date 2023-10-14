from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open the main page')
def open_soft_reelly(context):
    context.app.main_page.open_soft_reelly()


@when('Click on Secondary option at the left side menu')
def click_on_secondary(context):
    context.app.main_page.click_on_secondary()
