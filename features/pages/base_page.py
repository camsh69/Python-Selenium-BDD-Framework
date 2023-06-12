import logging
from utilities.LogUtil import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class BasePage(object):
    log = Logger(__name__, logging.INFO)

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_clickable(self, element, time=20):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(element))

    def is_element_visible(self, element, time=20):
        try:
            WebDriverWait(self.driver, time).until(EC.visibility_of(element))
            return True
        except TimeoutException:
            return False

    def enter_text(self, element, text):
        self.wait_for_element_to_be_clickable(element)
        element.clear()
        element.send_keys(text)

    def click_element(self, element):
        self.wait_for_element_to_be_clickable(element)
        element.click()

    def select_option_by_text(self, element, text):
        self.wait_for_element_to_be_clickable(element)
        dropdown = Select(element)
        dropdown.select_by_visible_text(text)

    def verify_link_presence(self, text):
        WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )
