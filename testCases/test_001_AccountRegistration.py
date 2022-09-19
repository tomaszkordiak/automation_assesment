from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utlilities.customLogger import LogGen
from utlilities.readProperties import ReadConfig
from utlilities.randomString import random_string_generator


class Test_001_AccountReg:
    baseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_account_reg(self, setup):
        self.logger.info("*** Test_001_AccountReg started ***")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.acceptCookies()
        self.hp.clickLogin()
        self.hp.clickOpenAccount()
        self.hp.clickOpenAccountButton()
        self.regpage = AccountRegistrationPage(self.driver)

        self.regpage.setFirstName(random_string_generator(size=10))
        self.regpage.setLastName(random_string_generator(size=10))
        self.regpage.setCountry("Poland")
        self.regpage.setAddress("Klinika Salve")
        self.regpage.setPhone("555555555")
        self.regpage.setEmail(random_string_generator() + "@gmail.com")
        self.regpage.clickEnterLoginDetailsBtn()
        self.regpage.selectEmailTypeOption()
        self.regpage.setPassword("AzTs12345")
        self.regpage.setConfPassword("AzTs12345")
        self.regpage.checkTermsConditions()
        self.regpage.clickCreateMyUserId()

        #         TBD
        # self.driver.close()
        self.logger.info("*** Test_001_AccountReg finished ***")
