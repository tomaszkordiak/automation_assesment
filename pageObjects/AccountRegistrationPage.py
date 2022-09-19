import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utlilities.customWaits import waitForElementOnPage


class AccountRegistrationPage:
    lbl_welcome_fedex_xpath = '//h1[contains(.,"Welcome to FedEx")]'
    lbl_enter_information_xpath = '//h2[contains(.,"Enter your contact information")]'
    input_first_name_xpath = '//input[@id="first-name"]'
    input_last_name_id = 'last-name'
    select_country_id = 'country'
    input_address_id = 'address'
    input_postal_code_id = 'postal-code'
    input_city_id = 'city'
    input_phone_id = 'phone'
    input_email_id = 'email'
    btn_enter_login_details_xpath = '//button[normalize-space()="Enter login details"]'
    radio_email_option_xpath = '//label[@for="emailTypeOption"]'
    radio_userid_option_id = 'userIdTypeOption'
    input_pass_id = 'password'
    input_confirm_pass_id = 'confirmPassword'
    chk_terms_conditions_id = 'acceptPrivacyPolicyAndTermsAndConditions-label'
    btn_submit_xpath = '//button[normalize-space()="Create my User ID"]'

    def __init__(self, driver):
        self.driver = driver

    def getWelcomeText(self):
        try:
            return self.driver.find_element(By.XPATH, self.lbl_welcome_fedex_xpath).text
        except:
            None

    def getPromptText(self):
        try:
            return self.driver.find_element(By.XPATH, self.lbl_enter_information_xpath).text
        except:
            None

    def setFirstName(self, fname):
        self.driver.find_element(By.ID, self.input_first_name_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.input_last_name_id).send_keys(lname)

    def setCountry(self, country):
        Select(self.driver.find_element(By.ID, self.select_country_id)).select_by_visible_text(country)

    def setAddress(self, address):
        self.driver.find_element(By.ID, self.input_address_id).send_keys(address)
        self.driver.find_element(By.XPATH, f'//span[@class="pac-matched"][contains(.,"{address}")]').click()

    def setPostCode(self, postcode):
        self.driver.find_element(By.ID, self.input_postal_code_id).send_keys(postcode)

    def setCity(self, city):
        self.driver.find_element(By.ID, self.input_city_id).send_keys(city)

    def setPhone(self, phone):
        self.driver.find_element(By.ID, self.input_phone_id).send_keys(phone)

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.input_email_id).send_keys(email)
        time.sleep(2)

    def clickEnterLoginDetailsBtn(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_enter_login_details_xpath))).click()
        waitForElementOnPage(self.driver, 20, By.XPATH, self.radio_email_option_xpath)

    def selectEmailTypeOption(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.radio_email_option_xpath))).click()

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.input_pass_id).send_keys(password)

    def setConfPassword(self, password):
        self.driver.find_element(By.ID, self.input_confirm_pass_id).send_keys(password)

    def checkTermsConditions(self):
        self.driver.find_element(By.ID, self.chk_terms_conditions_id).click()

    def clickCreateMyUserId(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()
        waitForElementOnPage(self.driver, 20, By.XPATH, '//h1[contains(.,"Finally, what type of shipping account do '
                                                        'you need?")]')


