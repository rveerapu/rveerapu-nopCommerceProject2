import time
import pytest
from pageObjects.loginPage import login
from pageObjects.addCustomerPage import AddCustomer
from pageObjects.searchCustomerPage import SearchCustomer
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseURL = readConfig.get_applicationUrl()
    email = readConfig.get_email()
    password = readConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = login(self.driver)
        self.lp.set_emailId(self.email)
        self.lp.set_passwordId(self.password)
        self.lp.click_loginButton()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Name **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        time.sleep(2)

        self.logger.info("************* searching customer by Name **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")
