from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class HomePage(BasePage):
    name = (By.NAME, "name")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.ID, "exampleInputPassword1")
    checkBox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submitBtn = (By.XPATH, "//input[@type='submit']")
    message = (By.CLASS_NAME, "alert-success")

    def select_name(self):
        element = self.driver.find_element(*HomePage.name)
        self.wait_for_element_to_be_clickable(element)
        return element

    def select_email(self):
        element = self.driver.find_element(*HomePage.email)
        self.wait_for_element_to_be_clickable(element)
        return element

    def select_password(self):
        element = self.driver.find_element(*HomePage.password)
        self.wait_for_element_to_be_clickable(element)
        return element

    def select_check_box(self):
        element = self.driver.find_element(*HomePage.checkBox)
        self.wait_for_element_to_be_clickable(element)
        return element

    def select_gender(self):
        element = self.driver.find_element(*HomePage.gender)
        self.wait_for_element_to_be_clickable(element)
        return element

    def select_submit(self):
        element = self.driver.find_element(*HomePage.submitBtn)
        self.wait_for_element_to_be_clickable(element)
        return element

    def select_message(self):
        element = self.driver.find_element(*HomePage.message)
        self.is_element_visible(element)
        return element

    def enter_name(self, name):
        self.select_name().send_keys(name)
        self.log.logger.info(f"Typing in a name with value {name}")

    def enter_email(self, email):
        self.select_email().send_keys(email)
        self.log.logger.info(f"Typing in an email with value {email}")

    def enter_password(self, password):
        self.select_password().send_keys(password)
        self.log.logger.info(f"Typing in a password with value {password}")

    def check_checkbox(self):
        self.select_check_box().click()
        self.log.logger.info("Clicking on a Checkbox")

    def enter_gender(self, gender):
        self.select_option_by_text(self.select_gender(), gender)
        self.log.logger.info(f"Selecting a dropdown option with value {gender}")

    def click_submit(self):
        self.select_submit().click()
        self.log.logger.info("Clicking on submit button")
