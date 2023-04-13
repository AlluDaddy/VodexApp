import time
from Pages.AudiencePage import Audience
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Campaign(BasePage):
    CAMPAIGN_LINK = (By.XPATH, "*//span[contains(text(),'Campaign')]")
    ADD_CAMPAIGN_BUTTON = (By.XPATH, "*//button[contains(text(),' Add Campaign')]")
    CAMPAIGN_NAME = (By.XPATH, '*//input[contains(@id,"id_Give")]')
    AUDIENCE_LIST_DROPDOWN = (By.ID, 'search_input')
    AUDIENCE_LIST_DROPDOWN_VAL = (By.XPATH, '//div[@class="optionListContainer displayNone"]/ul/li[@class="option    "]')
    CAMPAIGN_SAVE = (By.XPATH, "//button[@type='submit' and text()='Save'] ")

    def __init__(self, driver):
        super().__init__(driver)

    def create_campaign(self):
        self.do_clickon(self.CAMPAIGN_LINK)
        time.sleep(5)
        print("clicked on campaign link")
        try:
            print("campaign try link")
            if self.is_visible(self.ADD_CAMPAIGN_BUTTON):
                print("Campaign button is found")
                self.do_clickon(self.ADD_CAMPAIGN_BUTTON)
        except Exception as e:
            assert False, f"page not loaded - {e}"
        self.new_campaign_data()

    def new_campaign_data(self):
        self.do_clickon(self.AUDIENCE_LIST_DROPDOWN)
        time.sleep(2)
        res = self.driver.find_elements(By.XPATH,'//div[contains(@class,"optionListContainer")]/ul/li[@class="option    "]')
        lst = {}
        for i in res:
            lst[i.text] = i
        x = lst[TestData.AUDIENCE_NAME]
        x.click()
        self.do_send_keys(self.CAMPAIGN_NAME, TestData.CAMPAIGN_NAME)
        time.sleep(10)
        self.do_clickon(self.CAMPAIGN_SAVE)
        time.sleep(10)

    def trigger_call(self):
        # global cols
        table = self.driver.find_element(By.CLASS_NAME, 'table')
        body = table.find_element(By.TAG_NAME, 'tbody')
        rows = body.find_elements(By.TAG_NAME, 'tr')
        for i in rows:
            cells = body.find_elements(By.TAG_NAME, 'td')
            print(rows)
            cols = i.find_elements(By.TAG_NAME, 'td')
            if cols[0].text == TestData.CAMPAIGN_NAME:
                print(f"you added {cols[0].text} and {TestData.CAMPAIGN_NAME}")
                cols[3].click()
                time.sleep(15)
<<<<<<< HEAD
                break
=======
                break

                
#      stale exception:- wait.until(ExpectedConditions.refreshed(ExpectedConditions.stalenessOf("table")))
>>>>>>> 33fa542637eef28a171aac5a2a947dc0421eb98f
