import time
from pages.AudiencePage import Audience
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from config.config import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Campaign(BasePage):

    def __init__(self, driver):
        self.CAMPAIGN_LINK = (By.XPATH, "*//span[contains(text(),'Campaign')]")
        self.ADD_CAMPAIGN_BUTTON = (By.XPATH, "*//button[contains(text(),' Add Campaign')]")
        self.CAMPAIGN_NAME = (By.XPATH, '*//input[contains(@id,"id_Give")]')
        self.AUDIENCE_LIST_DROPDOWN = (By.ID, 'search_input')
        self.AUDIENCE_LIST_DROPDOWN_VAL = (
        By.XPATH, '//div[@class="optionListContainer displayNone"]/ul/li[@class="option    "]')
        self.CAMPAIGN_SAVE = (By.XPATH, "//button[@type='submit' and text()='Save'] ")
        super().__init__(driver)

        # locstors file should create

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
        res = self.driver.find_elements(By.XPATH,
                                        '//div[contains(@class,"optionListContainer")]/ul/li[@class="option    "]')
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

        table = self.driver.find_element(By.CLASS_NAME, 'table')
        body = table.find_element(By.TAG_NAME, 'tbody')
        rows = body.find_elements(By.TAG_NAME, 'tr')
        for i in rows:
            table = self.driver.find_element(By.CLASS_NAME, 'table')
            cells = body.find_elements(By.TAG_NAME, 'td')
            print(rows)
            cols = i.find_elements(By.TAG_NAME, 'td')
            if cols[0].text == TestData.CAMPAIGN_NAME:
                print(f"you added {cols[0].text} and {TestData.CAMPAIGN_NAME}")
                cols[4].click()
                time.sleep(15)
                break
