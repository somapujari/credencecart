from selenium.webdriver.common.by import By


class RegisterCred:
    lnkregister_xpath = '//a[@href="https://automation.credence.in/register"]'
    name_inp_id = 'name'
    email_inp_id = 'email'
    password_inp_id = 'password'
    conform_passw_inp_id = 'password-confirm'
    register_btn_xpath = '//button[@type="submit"]'

    def __init__(self,driver):
        self.driver = driver

    def registerclick(self):
        self.driver.find_element(By.XPATH, self.lnkregister_xpath).click()

    def name_enater(self, name):
        self.driver.find_element(By.ID, self.name_inp_id).clear()
        self.driver.find_element(By.ID, self.name_inp_id).send_keys(name)

    def email_eneter(self, email):
        self.driver.find_element(By.ID, self.email_inp_id).clear()
        self.driver.find_element(By.ID, self.email_inp_id).send_keys(email)

    def password_enter(self, password):
        self.driver.find_element(By.ID, self.password_inp_id).clear()
        self.driver.find_element(By.ID, self.password_inp_id).send_keys(password)

    def conform_password_enter(self, password):
        self.driver.find_element(By.ID, self.conform_passw_inp_id).clear()
        self.driver.find_element(By.ID, self.conform_passw_inp_id).send_keys(password)

    def submit_register(self):
        self.driver.find_element(By.XPATH, self.register_btn_xpath).click()

    def verify_registration(self):
        act_title = self.driver.title
        if act_title == 'CredKart':
            print('registration is completed')
            assert True
        else:
            print('registration failed')
            assert False




