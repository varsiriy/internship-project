from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.secondary_option_page import SecondaryOptionPage

class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.secondary_option_page = SecondaryOptionPage(driver)


