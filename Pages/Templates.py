from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
import time


class Templates(BasePage):
    TEMPLATES_LINK = (By.XPATH, "*//span[contains(text(),'Templates')]")
    REAL_ESTATE_SELECT = (By.XPATH, "*//span[contains(text(),'Real Estate')]/../../div/div/span/button[text()='Select']")
    USE_TEMPLATE = (By.XPATH, '*//span/button[contains(@class,"btn-info")][text()="Use Template"]')
    PROCEED_ANYWAY = (By.XPATH, '*//button[text()="Proceed Anyway!"]')
    OKAY_BUTTON = (By.XPATH, '*//button[text()="Okay"]')
    ALREADY_USE_TEXT = (By.XPATH, '*//div[text()="Already in use"]')
    ANOTHER_TEMPLATE = (By.XPATH, '*//div[contains(text(),"Another Template")]')
    def __init__(self, driver):
        super().__init__(driver)

    def templates(self):
        self.do_clickon(self.TEMPLATES_LINK)
        time.sleep(5)
        self.do_clickon(self.REAL_ESTATE_SELECT)
        time.sleep(2)
        self.do_clickon(self.USE_TEMPLATE)
        try:
            if self.ANOTHER_TEMPLATE:
                self.do_clickon(self.PROCEED_ANYWAY)
        except Exception as e:
            if self.ALREADY_USE_TEXT:
                self.do_clickon(self.OKAY_BUTTON)
        time.sleep(20)

