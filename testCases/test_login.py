from pageObjects import loginPage
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen
import pytest

class Test_001_login:
    baseUrl = readConfig.get_applicationUrl()
    email = readConfig.get_email()
    password = readConfig.get_password()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*************Test_001_login**************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True, "login Success"
        else:
            self.driver.get_screenshot_as_file("C:\\Users\\mohan\\nopComProject\\screenshots\\test_homePageTitle.png")
            assert False, "login Failed"
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = loginPage.login(self.driver)
        self.lp.set_emailId(self.email)
        self.lp.set_passwordId(self.password)
        self.lp.click_loginButton()
        act_title = self.driver.title
        assert act_title == "Dashboard / nopCommerce administration"
        self.driver.close()

# to run parallel processing with 2 workers
# pytest -s -v -n=2 test_login.py --browser_name chrome
# to generate html report
# pytest --html=..\reports\report.html test_login.py