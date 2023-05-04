import pytest
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def do_clickon(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator)).click()

    def do_send_keys(self, locator, text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return element.text

    def is_visible(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return bool(element)

    def get_title(self, title):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(title))
        return element

    def get_all_elements(self, locator):
        elements = WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def select_text(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        select = Select(element)
        # select = Select(self.driver.find_element_by_id('fruits01'))
        select.select_by_visible_text(text)
        # select.select_by_visible_text('Banana')

    # def ele_presence_wait(self):







