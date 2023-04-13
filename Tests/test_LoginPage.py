import time

import pytest

from Tests.conftest import Test_BasicTest
from Tests.test_base import BaseTest
from Config.config import TestData
from Pages.LoginPage import Login


class TestMain(Test_BasicTest):
    def test_main(self):
        # self.login_page.register(TestData.USER_NAME, TestData.PASSWORD)
        self.login_page.login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(10)
    #
    def test_dashboard(self):
        self.dashboard_page.get_all_data()
        self.dashboard_page.account_bal()
        self.dashboard_page.val_account_bal()
        time.sleep(10)

    def test_templates(self):
        self.template_page.templates()
        time.sleep(10)

    def test_recording(self):
        self.recording_page.recordings()
        time.sleep(10)

    def test_audience(self):
        self.audience_page.create_audience()
        time.sleep(10)

    def test_campaign(self):
        self.campaign_page.create_campaign()
        self.campaign_page.trigger_call()

