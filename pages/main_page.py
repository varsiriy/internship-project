from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MainPage(Page):
    SECONDARY_BTN = (By.CSS_SELECTOR, 'div.div-block-33 div.menu-button-text')

    def open_soft_reelly(self):
        self.driver.get('https://soft.reelly.io/sign-in')
        sleep(4)

    def click_on_secondary(self):
        self.click(*self.SECONDARY_BTN)