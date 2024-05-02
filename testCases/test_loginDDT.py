import time
import pytest
from pageObjects import loginPage
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen
from utilities import XLUtility

class Test_001_login_DDT:

    baseUrl = readConfig.get_applicationUrl()
    fileExcel = "C:\\Users\\mohan\\nopComProject\\TestData\\loginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = loginPage.login(self.driver)
        sheet = XLUtility.openWorkbookSheet(self.fileExcel, "Sheet1")
        rows = XLUtility.getRowCount(sheet)
        list_status = []
        for row in range(2, rows+1):
            emailId = XLUtility.readData(sheet, row, 1)
            password = XLUtility.readData(sheet, row, 2)
            exp = XLUtility.readData(sheet, row, 3)
            self.lp.set_emailId(emailId)
            self.lp.set_passwordId(password)
            self.lp.click_loginButton()
            time.sleep(3)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if exp == 'pass':
                    self.logger.info("******* Test passed")
                    list_status.append("Pass")
                    self.lp.click_logout()
                else:
                    self.logger.info("******* Test failed")
                    list_status.append("Fail")
                    self.lp.click_logout()
            else:
                if exp == 'fail':
                    self.logger.info("******* Test passed")
                    list_status.append("Pass")
                else:
                    self.logger.info("******* Test failed")
                    list_status.append("Fail")
        if "Fail" in list_status:
            self.logger.info("Login DDT failed")
            assert False
        else:
            self.logger.info("Login DDT Passed")
            assert True
        self.driver.close()
        self.logger.info("")
