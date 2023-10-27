from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def draw_element_on_screenshot(element, param):
    pass


class MainPage(Page):
    SECONDARY_BTN = (By.CSS_SELECTOR, 'div.div-block-33 div.menu-button-text')
    MOB_SECONDARY_BTN = (By.CSS_SELECTOR, 'a.menu-link[href="/secondary-listings"]')

    def open_soft_reelly(self):
        self.driver.get('https://soft.reelly.io/sign-in')
        sleep(4)

    def click_on_secondary(self):
        # locator = self.SECONDARY_BTN
        #
        # element = self.driver.find_element(*locator)
        #
        # print(f"Element location: {element.location}")
        # print(f"Element size: {element.size}")
        #
        # self.driver.save_screenshot('debug.png')
        # draw_element_on_screenshot(element, 'debug.png')

        # self.wait_for_element_clickable(*self.SECONDARY_BTN)
        # self.click(*self.SECONDARY_BTN)

        # Mobile
        self.wait_for_element_clickable(*self.MOB_SECONDARY_BTN)
        self.click(*self.MOB_SECONDARY_BTN)




