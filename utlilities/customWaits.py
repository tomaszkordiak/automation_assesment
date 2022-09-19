from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def waitForElementOnPage(driver, delay, locator_strategy, locator):
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((locator_strategy, locator)))
        print
        "Page is ready!"
    except TimeoutException:
        print
        "Loading took too much time!"
