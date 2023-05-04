import time

from ..Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from ..Config.config import TestData


class Login(BasePage):
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    CPASSWORD = (By.NAME, 'cpassword')
    LOGIN_BUTTON = (By.CLASS_NAME, 'login100-form-btn')
    REGISTER_LINK = (By.XPATH, '*//div/a[contains(text(),"Or Register")]')
    AGREE = (By.XPATH, "*//input[contains(@class,'form-check-input')]")
    REGISTER = (By.XPATH, '*//button[contains(@type,"submit")][text()="Register"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()

    def get_login_page_title(self, title):
        return self.get_title(title)

    def login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_clickon(self.LOGIN_BUTTON)
        print("Login")
        time.sleep(10)

    def register(self, username, password):
        self.do_clickon(self.REGISTER_LINK)
        time.sleep(1)
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_send_keys(self.CPASSWORD, password)
        self.do_clickon(self.AGREE)
        self.do_clickon(self.REGISTER)
        time.sleep(10)

