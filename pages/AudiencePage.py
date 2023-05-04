import time

from ..Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from ..Config.config import TestData
from selenium.webdriver.support.ui import Select


class Audience(BasePage):
    AUDIENCE_LINK = (By.XPATH, "*//span[contains(text(),'Audience')]")
    AUDIENCE_LIST_BUTTON = (By.XPATH, "*//button[contains(text(),'New Audience List')]")
    AUDIENCE_NAME = (By.XPATH, '*//input[contains(@id,"id_Name")]')
    PHONE_NUM_DROPDOWN = (By.ID, 'input_category')
    FIRST_NAME = (By.ID, 'id_First Name')
    LAST_NAME = (By.ID, 'id_Last Name')
    PHONE_NUM = (By.ID, 'id_Phone')
    AUDIENCE_SAVE = (By.XPATH, "//button[@type='submit' and text()='Save'] ")
    AUDIENCE_DUP_POP = (By.XPATH, '//*[@class="modal-title h4"]')
    AUDIENCE_POP_SAVE = (By.XPATH, '*//button[contains(text(), "Save Changes")]')

    def __init__(self, driver):
        super().__init__(driver)

    def create_audience(self):
        self.do_clickon(self.AUDIENCE_LINK)
        print("audience clicked")

        try:
            if self.is_visible(self.AUDIENCE_LIST_BUTTON):
                print("audience list audience")
                self.do_clickon(self.AUDIENCE_LIST_BUTTON)
        except Exception as e:
            assert False, f"page not loaded - {e}"
        self.new_audience_data()

    def new_audience_data(self):
        self.do_send_keys(self.AUDIENCE_NAME, TestData.AUDIENCE_NAME)
        self.select_text(self.PHONE_NUM_DROPDOWN, TestData.PHONE_NUM_DROPDOWN)
        self.do_send_keys(self.FIRST_NAME, TestData.FIRST_NAME)
        self.do_send_keys(self.LAST_NAME, TestData.LAST_NAME)
        self.do_send_keys(self.PHONE_NUM, TestData.PHONE_NUM)
        time.sleep(3)
        self.do_clickon(self.AUDIENCE_SAVE)
        try:
            if self.is_visible(self.AUDIENCE_DUP_POP):
                self.do_clickon(self.AUDIENCE_POP_SAVE)
        except Exception as e:
            pass

        print("clicked on audience save")
        time.sleep(10)
