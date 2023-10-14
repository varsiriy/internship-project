from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class SecondaryOptionPage(Page):
    PAGIN_NEXT_BTN = (By.CSS_SELECTOR, 'a[wized="nextPageMLS"]')
    PAGIN_PREV_BTN = (By.CSS_SELECTOR, 'div[wized="previousPageMLS"]')
    PAGE_COUNT = (By.CSS_SELECTOR, 'div[wized="totalPageProperties"]')
    CURRENT_PG = (By.CSS_SELECTOR, 'div[wized="currentPageProperties"]')

    def verify_secondary_opened(self):
        self.verify_partial_url('https://soft.reelly.io/secondary-listings')
        sleep(5)

    def go_to_the_final_pg(self):
        page_count = int(self.find_element(*self.PAGE_COUNT).text)
        current_pg = int(self.find_element(*self.CURRENT_PG).text)

        while current_pg <= page_count:
            print(f"Current Page: {current_pg}, Total Pages: {page_count}")
            self.find_element(*self.PAGIN_NEXT_BTN).click()
            sleep(2)
            self.wait_for_element_clickable(*self.PAGIN_NEXT_BTN)
            current_pg += 1

        sleep(5)

    def back_to_the_first_pg(self):
        page_count = int(self.find_element(*self.PAGE_COUNT).text)
        current_pg = int(self.find_element(*self.CURRENT_PG).text)

        while current_pg >= 1:
            print(f"Current Page: {current_pg}, Total Pages: {page_count}")
            self.find_element(*self.PAGIN_PREV_BTN).click()
            sleep(2)
            self.wait_for_element_clickable(*self.PAGIN_PREV_BTN)
            current_pg -= 1
        print("Back on page 1")



