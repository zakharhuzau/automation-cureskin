from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from support.logger import logger, MyListener
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920x1080')
    context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options=options), MyListener())
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()