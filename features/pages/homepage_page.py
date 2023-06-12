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

    def enter_name(self, name):
        element = self.driver.find_element(*HomePage.name)
        self.enter_text(element, name)
        self.log.logger.info(f"Typing in a name with value {name}")

    def enter_email(self, email):
        element = self.driver.find_element(*HomePage.email)
        self.enter_text(element, email)
        self.log.logger.info(f"Typing in an email with value {email}")

    def enter_password(self, password):
        element = self.driver.find_element(*HomePage.password)
        self.enter_text(element, password)
        self.log.logger.info(f"Typing in a password with value {password}")

    def check_checkbox(self):
        element = self.driver.find_element(*HomePage.checkBox)
        self.click_element(element)
        self.log.logger.info("Clicking on a Checkbox")

    def enter_gender(self, gender):
        element = self.driver.find_element(*HomePage.gender)
        self.select_option_by_text(element, gender)
        self.log.logger.info(f"Selecting a dropdown option with value {gender}")

    def click_submit(self):
        element = self.driver.find_element(*HomePage.submitBtn)
        self.click_element(element)
        self.log.logger.info("Clicking on submit button")

    def select_message(self):
        element = self.driver.find_element(*HomePage.message)
        self.is_element_visible(element)
        self.log.logger.info("Message is visible")
        return element
