import time

from pageobjects.logincred import LoginCred
from pageobjects.addtocartcred import AddToCart
from pageobjects.billpaycred import Bill
from utility.readproperty import ReadConfig


class Test_BillPay:
    base_url = ReadConfig.get_appplication_url()
    email = ReadConfig.get_user_mail()
    password = ReadConfig.get_password()

    def test_billpayconform(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)

        self.lg = LoginCred(self.driver)
        self.lg.login_click()
        self.lg.emailenter(self.email)
        self.lg.password_enter(self.password)
        self.lg.login_submit_click()
        self.lg.verify_login()

        self.ad = AddToCart(self.driver)
        self.ad.macbook_click()
        self.ad.add_to_cart_click()
        self.ad.verify_ass_to_cart()

        time.sleep(5)




