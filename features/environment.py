import allure
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from utilities import configReader


def before_scenario(context, driver):
    url = configReader.readConfig("config", "url")
    browser = configReader.readConfig("config", "browser")
    headless = configReader.readConfig("config", "headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless == "true":
            options.add_argument("--headless")
            options.add_argument("--start-maximized")
        context.driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        context.driver = webdriver.Firefox()
    elif browser == "edge":
        context.driver = webdriver.Edge()

    # context.driver.implicitly_wait(5)
    context.driver.set_page_load_timeout(30)
    context.driver.maximize_window()

    try:
        context.driver.get(url)
    except TimeoutException:
        pass


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
