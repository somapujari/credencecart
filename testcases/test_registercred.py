import random
import string
import time
from utility.readproperty import ReadConfig

from pageobjects.credregister import RegisterCred
from utility.customerlogger import LogGen


class Test_Registration:
    base_url = ReadConfig.get_appplication_url()
    name = 'soma'
    # email = 'credence11@gmail.com'
    password = 'test@123'
    logger = LogGen.loggen()

    def test_register(self, setup):
        self.logger.debug('*************test_register ******')
        self.driver = setup
        self.logger.debug('*********** opening the url ***********')
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.re = RegisterCred(self.driver)
        self.logger.debug('***** clicking on the register link ******')
        self.re.registerclick()
        self.logger.info('********** enter a username*****')
        self.re.name_enater(self.name)
        self.email = self.random_email_generator()+'@gmail.com'
        self.logger.info('*********entering a email  *****')
        self.re.email_eneter(self.email)
        self.logger.info('************* entering  a password *****')
        self.re.password_enter(self.password)
        self.logger.info('entering a password')
        self.re.conform_password_enter(self.password)
        self.logger.info('*********clicking the register lin ******* ')
        self.re.submit_register()
        self.logger.info('*****verifing the registeration *** ')
        self.re.verify_registration()
        self.logger.info('test_registeration is compleated ****')
        time.sleep(5)

    def random_email_generator(self, size=8, char=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(char) for i in range(size))



