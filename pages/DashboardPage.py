import time

from ..Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from ..Config.config import TestData


class Dashboard(BasePage):
    ALL_RECORDS = (By.XPATH, "//*[contains(@class, 'card border-left')]")

    def __init__(self, driver):
        super().__init__(driver)
        # self.acc_balance = None
        # self.elements = None

    def get_all_data(self):
        global elements
        try:
            elements = self.get_all_elements(self.ALL_RECORDS)
            self.elements = [i.text for i in elements]
        except:
            assert False, "page not loaded"
        return self.elements

    def account_bal(self):
        global acc_balance
        self.acc_balance = int(self.elements[0][17:])
        return self.acc_balance

    def val_account_bal(self):
        if self.acc_balance>=4:
            return True
        else:
            assert False, "Not enough balance"



