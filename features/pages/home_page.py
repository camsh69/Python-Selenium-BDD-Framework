from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
import logging
from utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class HomePage(BasePage):
    name = (By.NAME, "name")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.ID, "exampleInputPassword1")
    checkBox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submitBtn = (By.XPATH, "//input[@type='submit']")
    message = (By.CLASS_NAME, "alert-success")

    def selectName(self):
        element = self.driver.find_element(*HomePage.name)
        self.wait_for_element_to_be_clickable(element)
        return element

    def selectEmail(self):
        element = self.driver.find_element(*HomePage.email)
        self.wait_for_element_to_be_clickable(element)
        return element

    def selectPassword(self):
        element = self.driver.find_element(*HomePage.password)
        self.wait_for_element_to_be_clickable(element)
        return element

    def selectCheckBox(self):
        element = self.driver.find_element(*HomePage.checkBox)
        self.wait_for_element_to_be_clickable(element)
        return element

    def selectGender(self):
        element = self.driver.find_element(*HomePage.gender)
        self.wait_for_element_to_be_clickable(element)
        return element

    def selectSubmit(self):
        element = self.driver.find_element(*HomePage.submitBtn)
        self.wait_for_element_to_be_clickable(element)
        return element

    def selectMessage(self):
        element = self.driver.find_element(*HomePage.message)
        return element

    def enterName(self, name):
        self.selectName().send_keys(name)
        log.logger.info("Typing in an Element with value " + str(name))

    def enterEmail(self, email):
        self.selectEmail().send_keys(email)
        log.logger.info("Typing in an Element with value " + str(email))

    def enterPassword(self, password):
        self.selectPassword().send_keys(password)
        log.logger.info("Typing in an Element with value " + str(password))

    def checkCheckBox(self):
        self.selectCheckBox().click()
        log.logger.info("Clicking on an Checkbox")

    def enterGender(self, gender):
        self.selectOptionByText(self.selectGender(), gender)
        log.logger.info("Selecting an Element with value " + str(gender))

    def clickSubmit(self):
        self.selectSubmit().click()
        log.logger.info("Clicking on submit button")
