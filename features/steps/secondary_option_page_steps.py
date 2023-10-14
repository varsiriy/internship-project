from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@then('Verify the right page opens')
def verify_secondary_opened(context):
    context.app.secondary_option_page.verify_secondary_opened()



@then('Go to the final page using the pagination button')
def go_to_the_final_pg(context):
    context.app.secondary_option_page.go_to_the_final_pg()


@then('Go back to the first page using the pagination button')
def back_to_the_first_pg(context):
    context.app.secondary_option_page.back_to_the_first_pg()
