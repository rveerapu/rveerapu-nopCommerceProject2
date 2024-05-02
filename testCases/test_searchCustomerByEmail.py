import time
import pytest
from pageObjects.loginPage import login
from pageObjects.addCustomerPage import AddCustomer
from pageObjects.searchCustomerPage import SearchCustomer
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURL = readConfig.get_applicationUrl()
    email = readConfig.get_email()
    password = readConfig.get_password()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = login(self.driver)
        self.lp.set_emailId(self.email)
        self.lp.set_passwordId(self.password)
        self.lp.click_loginButton()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info("************* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")
