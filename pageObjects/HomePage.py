from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    lnk_login_xpath = '//span[text()="Sign Up/Log In "]'
    lnk_open_account_xpath = '//a[@id="fxg-dropdown-signIn"]//following-sibling::div//a[@title="Open an Account"]'
    btn_accept_cookies_xpath = '//button[contains(.,"ACCEPT ALL COOKIES")]'
    btn_open_account_xpath = '//a[@title="Open a free account"]'

    def __init__(self, driver):
        self.driver = driver

    def acceptCookies(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_accept_cookies_xpath))).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.lnk_login_xpath).click()

    def clickOpenAccount(self):
        self.driver.find_element(By.XPATH, self.lnk_open_account_xpath).click()

    def clickOpenAccountButton(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_open_account_xpath))).click()

