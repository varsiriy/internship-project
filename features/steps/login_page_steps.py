from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

EMAIL_FIELD = ()
PASSWORD_FIELD = ()
CONTINUE_BTN = ()


@given('Log in to the page')
def login_on_soft_reelly(context):
    context.app.login_page.login_on_soft_reelly()