from selenium.webdriver.common.by import By

class login:
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type = 'submit']"
    link_logout_xpath = "//a[@href = '/logout']"

    def __init__(self, driver):
        self.driver = driver

    def set_emailId(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def set_passwordId(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_loginButton(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()