import allure
from selenium import webdriver
from utilities import configReader


def before_scenario(context, driver):
    url = configReader.readConfig("basic info", "url")
    if configReader.readConfig("basic info", "browser") == "chrome":
        options = webdriver.ChromeOptions()
        if configReader.readConfig("basic info", "headless") == "true":
            options.add_argument("--headless")
            options.add_argument("--start-maximised")
        context.driver = webdriver.Chrome(options=options)
        # elif configReader.readConfig("basic info", "browser") == "firefox":
        #     context.driver = webdriver.Firefox()
        # elif configReader.readConfig("basic info", "browser") == "edge":
        #     context.driver = webdriver.Edge()

        context.driver.implicitly_wait(5)
        context.driver.set_page_load_timeout(30)
        context.driver.maximize_window()
        context.driver.get(url)


def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    print()
    if step.status == "failed":
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG,
        )
