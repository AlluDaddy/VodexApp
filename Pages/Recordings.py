from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
import time


class Recording(BasePage):
    RECORDINGS_LINK = (By.XPATH, "*//span[contains(text(),'Recordings')]")
    ADD_RECORDING = (By.XPATH, "*//button[contains(text(),' Add Recording')]")
    RECORDINGS_LIST_DROPDOWN = (By.ID, "input_category")
    RECORDINGS_SAVE = (By.XPATH, '*//button[contains(text(),"Save")][@type="submit"]')
    RECORDINGS_SUCCESS_SAVE = (By.XPATH, '*//button[contains(text(),"Okay")][@type="button"]')
    PATH_WELCOME = "C:\\Users\\User\\Downloads\\welcome.mp3"
    PATH_BYE = "C:\\Users\\User\\Downloads\\Bye-bye.mp3"

    def __init__(self, driver):
        super().__init__(driver)

    def recordings(self):
        self.do_clickon(self.RECORDINGS_LINK)
        time.sleep(5)
        print("clicked on campaign link")
        self.table = self.driver.find_element(By.CLASS_NAME, 'table')
        self.body = self.table.find_element(By.TAG_NAME, 'tbody')
        self.rows = self.body.find_elements(By.TAG_NAME, 'tr')
        self.cells = self.body.find_elements(By.TAG_NAME, 'td')
        self.upload_record(TestData.GREET_TAG_NAME, self.PATH_WELCOME)
        scroll_bar = self.driver.find_element(By.XPATH, ' *//div[contains(@class,"table-responsive")]')
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                   scroll_bar)
        time.sleep(20)
        self.upload_record(TestData.FALLBACK_TAG_NAME, self.PATH_BYE)

    def upload_record(self, tag_name, recording_path):
        for i in self.rows:
            self.cols = i.find_elements(By.TAG_NAME, 'td')
            print(self.cols[1].text)
            if self.cols[1].text == tag_name:
                self.cols[4].click()
        self.do_clickon(self.RECORDINGS_LIST_DROPDOWN)
        time.sleep(10)
        res = self.select_text(self.RECORDINGS_LIST_DROPDOWN, "Upload a Recording File")
        time.sleep(10)
        s = self.driver.find_element(By.XPATH, "*//div/input[@type='file']")
        s.send_keys(recording_path)
        time.sleep(10)
        self.do_clickon(self.RECORDINGS_SAVE)
        try:
            self.do_clickon(self.RECORDINGS_SUCCESS_SAVE)
        except:
            pass
