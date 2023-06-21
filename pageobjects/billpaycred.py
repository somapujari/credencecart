from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Bill:
    procede_pay_lnk_Xpath = '//a[@href="/checkout"]'
    first_name_inp_id = 'first_name'
    last_name_inp_id = "last_name"
    phonenumber_inp_id = 'phone'
    address_inp_id = 'address'
    zip_inp_id = 'zip'
    state_inp_id = 'state'
    city_sele_xpath = "//select[@id='state']/option"
    owner_name_inp_id = 'owner'
    cvv_inp_id = 'cvv'
    card_number_inp_id = 'cardNumber'
    exp_year_cli_id = 'exp_year'
    exp_year_sel_Xpath = '//select[@id="exp_year"]/option'
    exp_month_cli_id = 'exp_month'
    exp_month_sel_Xpath = '//select[@id="exp_month"]/option'
    conform_btn_id = 'confirm-purchase'
    body_contains_Xpath = '//body'

    def __init__(self, driver):
        self.drop = None
        self.driver = driver

    def proced_tocheckout_click(self):
        self.driver.find_element(By.XPATH, self.procede_pay_lnk_Xpath).click()

    def first_name_enter(self, first_name):
        self.driver.find_element(By.ID, self.first_name_inp_id).clear()
        self.driver.find_element(By.ID, self.first_name_inp_id).send_keys(first_name)

    def last_name_enter(self, last_name):
        self.driver.find_element(By.ID, self.last_name_inp_id).clear()
        self.driver.find_element(By.ID, self.last_name_inp_id).send_keys(last_name)

    def phonenumber_enter(self, phone):
        self.driver.find_element(By.ID, self.phonenumber_inp_id).clear()
        self.driver.find_element(By.ID, self.phonenumber_inp_id).send_keys(phone)

    def address_enter(self,address):
        self.driver.find_element(By.ID, self.address_inp_id).clear()
        self.driver.find_element(By.ID, self.address_inp_id).send_keys(address)

    def zip_enter(self, zip):
        self.driver.find_element(By.ID, self.zip_inp_id).clear()
        self.driver.find_element(By.ID, self.zip_inp_id).send_keys(zip)

    # def state_select(self,state):
    #     selectel = self.driver.find_element(By.ID, self.state_inp_id)
    #     self.drop = Select(selectel)
    #     self.drop.select_by_visible_text(state)

    def city_select(self, city):
        self.driver.find_element(By.ID, self.state_inp_id).click()
        options = self.driver.find_elements(By.XPATH, self.city_sele_xpath)
        for option in options:
            if option.text == city:
                option.click()
                break

    def card_ownername_enter(self, owner_name):
        self.driver.find_element(By.ID, self.owner_name_inp_id).clear()
        self.driver.find_element(By.ID, self.owner_name_inp_id).send_keys(owner_name)

    def cvv_enter(self, cvv):
        self.driver.find_element(By.ID, self.cvv_inp_id).clear()
        self.driver.find_element(By.ID, self.cvv_inp_id).send_keys(cvv)

    def card_number_enter(self, card_number):
        self.driver.find_element(By.ID, self.card_number_inp_id).clear()
        for i in range(0,len(card_number), 4):
            chunk = card_number[i:i+4]
            self.driver.find_element(By.ID, self.card_number_inp_id).send_keys(chunk)

    def exp_year_select(self, exp_year):
        self.driver.find_element(By.ID,self.exp_year_cli_id).click()
        options = self.driver.find_elements(By.XPATH, self.exp_year_sel_Xpath)
        for option in options:
            if option.text == exp_year:
                option.click()
                break

    def exp_mont_select(self, exp_month):
        self.driver.find_element(By.ID, self.exp_month_cli_id).click()
        options = self.driver.find_elements(By.XPATH, self.exp_month_sel_Xpath)
        for option in options:
            if option.text == exp_month:
                option.click()
                break

    def continue_to_conform(self):
        self.driver.find_element(By.ID, self.conform_btn_id).click()

    def verify_order(self):
        conform_tex = self.driver.find_element(By.XPATH, self.body_contains_Xpath).text
        if 'Your order has been placed successfully.' in conform_tex:
            assert True
        else:
            assert False
