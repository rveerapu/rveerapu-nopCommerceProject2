import configparser

config = configparser.ConfigParser()
config.read("C:\\Users\\mohan\\nopComProject\\configurations\\config.ini")

class readConfig:
    @staticmethod
    def get_applicationUrl():
        baseUrl = config['common_info']['baseUrl']
        return baseUrl

    @staticmethod
    def get_email():
        email = config['common_info']['email']
        return email

    @staticmethod
    def get_password():
        password = config['common_info']['password']
        return password
