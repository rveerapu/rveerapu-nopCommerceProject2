import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.loginPage import login
from pageObjects.addCustomerPage import AddCustomer
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = readConfig.get_applicationUrl()
    username = readConfig.get_email()
    password = readConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = login(self.driver)
        self.lp.set_emailId(self.username)
        self.lp.set_passwordId(self.password)
        self.lp.click_loginButton()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()

        self.logger.info("************* Providing customer info **********")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Ram")
        self.addcust.setLastName("Sree")
        self.addcust.setDob("7/05/1985")  # Format: D / MM / YYY
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing.........")
        self.addcust.clickOnSave()
        self.logger.info("************* Saving customer info **********")
        self.logger.info("********* Add customer validation started *****************")
        self.msg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot("C:\\Users\\mohan\\nopComProject\\screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False
        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
