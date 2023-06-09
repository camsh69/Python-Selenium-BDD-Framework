from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_clickable(self, element, time=20):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(element))

    def is_element_visible(self, element, time=20):
        try:
            WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located(element)
            )
            return True
        except TimeoutException:
            return False

    def selectOptionByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def verify_link_presence(self, text):
        WebDriverWait(self.driver, 7).until(
            EC.presence_of_element_located((By.LINK_TEXT, text))
        )
