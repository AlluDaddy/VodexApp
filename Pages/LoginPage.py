from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData


class Login(BasePage):
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'login100-form-btn')
    REGISTER_LINK = (By.XPATH, '//*[@id="wrapper"]/div/div/div/form/div[7]/a')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()

    def get_login_page_title(self, title):
        return self.get_title(title)

    def register_link(self):
        return self.is_visible(self.REGISTER_LINK)

    def login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_clickon(self.LOGIN_BUTTON)
