from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

EMAIL_FIELD = (By.CSS_SELECTOR, 'input[type="email"]')
PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[type="password"]')
CONTINUE_BTN = (By.CSS_SELECTOR, 'a.login-button')


class LoginPage(Page):
    def login_on_soft_reelly(self):
        email_input = self.find_element(*EMAIL_FIELD)
        email_input.clear()
        email_input.send_keys('varsiriy@gmail.com')

        password_inputs = self.find_element(*PASSWORD_FIELD)
        password_inputs.clear()
        password_inputs.send_keys('1234Qwerty')

        self.click(*CONTINUE_BTN)
        sleep(4)
