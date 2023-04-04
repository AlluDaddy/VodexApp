from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
import time

class Recording(BasePage):
    RECORDINGS_LINK = (By.XPATH, "*//span[contains(text(),'Recordings')]")
    ADD_RECORDING = (By.XPATH, "*//button[contains(text(),' Add Recording')]")
    RECORDINGS_LIST_DROPDOWN = (By.ID, "input_category")

    def __init__(self, driver):
        super().__init__(driver)
        # self.acc_balance = None
        # self.elements = None

    def recordings(self):
        self.do_clickon(self.RECORDINGS_LINK)
        time.sleep(5)
        print("clicked on campaign link")

        table = self.driver.find_element(By.CLASS_NAME, 'table')
        body = table.find_element(By.TAG_NAME, 'tbody')
        rows = body.find_elements(By.TAG_NAME, 'tr')
        cells = body.find_elements(By.TAG_NAME, 'td')

        print(len(rows))
        print(len(cells))
        for i in rows:
            cols = i.find_elements(By.TAG_NAME, 'td')
            # cols = self.get_all_elements((By.TAG_NAME, 'td'))
            print(cols[1].text)

            # cols = i.find_elements(By.TAG_NAME, 'td')
            if cols[1].text == TestData.GREET_TAG_NAME:
            #     print(f"you added {cols[0].text} and {TestData.CAMPAIGN_NAME}")
                cols[4].click()
            #     time.sleep(15)
                self.upload_record()

    def upload_record(self):
        self.do_clickon(self.RECORDINGS_LIST_DROPDOWN)
        time.sleep(2)
        res = self.driver.find_elements(By.XPATH,
                                        '//*/select/option[2]')
        s = self.driver.find_element(By.XPATH, "//input[@type='file']")
        s.send_keys("C:\\Users\\User\\Downloads\\welcome.mp3")
        # lst = {}
        # for i in res:
        #     lst[i.text] = i
        # x = lst[TestData.AUDIENCE_NAME]
        # x.click()
        # self.do_send_keys(self.CAMPAIGN_NAME, TestData.CAMPAIGN_NAME)
        # time.sleep(10)
        # self.do_clickon(self.CAMPAIGN_SAVE)
        # time.sleep(10)