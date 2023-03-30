import pytest

from Tests.conftest import Test_BasicTest
from Tests.test_base import BaseTest
from Config.config import TestData
from Pages.LoginPage import Login


class Test_Main(Test_BasicTest):
    def test_main(self):
        self.login_page.login(TestData.USER_NAME, TestData.PASSWORD)
        # self.dashboard_page.get_all_data()
        # self.dashboard_page.account_bal()
        # self.dashboard_page.val_account_bal()
        self.audience_page.create_audience()
        self.campaign_page.create_campaign()
        self.campaign_page.run_campaign()
