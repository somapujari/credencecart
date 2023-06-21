import time

from pageobjects.logincred import LoginCred
from pageobjects.addtocartcred import AddToCart
from utility.readproperty import ReadConfig
from pageobjects.billpaycred import Bill
from utility.customerlogger import LogGen


class Test_AddToCart:
    base_url = ReadConfig.get_appplication_url()
    email = ReadConfig.get_user_mail()
    password = ReadConfig.get_password()
    first_name = 'soma'
    last_name = 'puja'
    phone = '8805633666'
    address = 'bijapur hoghway pune'
    zip = '411039'
    city = 'Chennai'
    owner_name = 'vishal panchal'
    cvv = '737'
    card_number = '5555444433331111'
    exp_year = '2025'
    exp_month = 'March'
    logger = LogGen.loggen()

    def test_addtocart(self, setup):
        self.logger.info('**** test_addtocart *********************** ')
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.lg = LoginCred(self.driver)
        self.lg.login_click()
        self.logger.info('******** entering email ****** ')
        self.lg.emailenter(self.email)
        self.logger.info('******** entering password ****** ')
        self.lg.password_enter(self.password)
        self.logger.info('******** clicking logon button  ****** ')
        self.lg.login_submit_click()
        self.logger.info('******** verifying login  ****** ')
        self.lg.verify_login()
        self.logger.info('************* test_login  is compleated ')

        self.logger.info(' ************** opening add to cart page ****  ')
        self.ad = AddToCart(self.driver)
        self.logger.info('******** clicking on product ****** ')
        self.ad.macbook_click()
        self.ad.add_to_cart_click()
        self.logger.info('******** verifying the  add to cart  ****** ')
        self.ad.verify_ass_to_cart()

        self.logger.info('************* billing page opening  **** *')
        self.bi = Bill(self.driver)
        self.bi.proced_tocheckout_click()
        self.logger.info('***** entering a name ******** ')
        self.bi.first_name_enter(self.first_name)
        self.logger.info('***** entering a lastname ******** ')
        self.bi.last_name_enter(self.last_name)
        self.logger.info('****** entering  aphone number ***** ')
        self.bi.phonenumber_enter(self.phone)
        self.bi.address_enter(self.address)
        self.bi.zip_enter(self.zip)
        self.logger.info('**********  selecting city  ************ ')
        self.bi.city_select(self.city)
        self.bi.card_ownername_enter(self.owner_name)
        self.logger.info('**************** entering cvv **** *** ')
        self.bi.cvv_enter(self.cvv)
        self.logger.info('******** entering card number ')
        self.bi.card_number_enter(self.card_number)

        self.bi.exp_year_select(self.exp_year)
        self.bi.exp_mont_select(self.exp_month)
        self.bi.continue_to_conform()
        self.logger.info('******** verifying the order ')
        self.bi.verify_order()
        self.logger.info('******* test is compleated *****')
        time.sleep(5)





