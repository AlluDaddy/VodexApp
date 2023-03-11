import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Config.config import TestData
from Pages.AudiencePage import Audience
from Pages.Campaign import Campaign
from Pages.DashboardPage import Dashboard
from Pages.LoginPage import Login
from Tests.test_base import BaseTest


@pytest.fixture(params=["chrome"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    # if request.param == "edge":
    #     driver = webdriver.Edge(executable_path= GeckoDriverManager().install())
    # if request.param == "chrome":
    #     driver = webdriver.Chrome(executable_path= TestData.DRIVER_PATH)
    # if request.param == "edge":
    #     driver = webdriver.Edge(executable_path = TestData.EDGE_PATH)
    request.cls.driver = driver
    yield
    driver.close()


#
# #
# @pytest.mark.usefixtures("driver_init")
class Test_BasicTest(BaseTest):
    # @pytest.fixture(autouse=True)
    def setup(self):
        self.login_page = Login(self.driver)
        self.dashboard_page = Dashboard(self.driver)
        self.audience_page = Audience(self.driver)
        self.campaign_page = Campaign(self.driver)



