import time

from pageobjects.logincred import LoginCred
from utility.readproperty import ReadConfig
from  utility.customerlogger import LogGen


class Test_Logoin:
    base_url = ReadConfig.get_appplication_url()
    email = ReadConfig.get_user_mail()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info('***** test_login *******  ')
        self.driver = setup
        self.logger.info('*****  opening url **** ')
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.lg = LoginCred(self.driver)
        self.lg.login_click()
        self.logger.info('****** entering email **** ')
        self.lg.emailenter(self.email)
        self.logger.info('************ entering password *** ')
        self.lg.password_enter(self.password)
        self.lg.login_submit_click()
        self.lg.verify_login()
        self.logger.info('***** test_login is compleated **** ')

        # time.sleep(5)




