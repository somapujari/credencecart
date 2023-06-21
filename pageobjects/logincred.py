from selenium.webdriver.common.by import By


class LoginCred:
    login_lnk_xpath = '//a[@href="https://automation.credence.in/login"]'
    email_inp_id = 'email'
    password_inp_id = 'password'
    login_btn_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def login_click(self):
        self.driver.find_element(By.XPATH, self.login_lnk_xpath).click()

    def emailenter(self, email):
        self.driver.find_element(By.ID, self.email_inp_id).clear()
        self.driver.find_element(By.ID, self.email_inp_id).send_keys(email)

    def password_enter(self, password):
        self.driver.find_element(By.ID, self.password_inp_id).clear()
        self.driver.find_element(By.ID, self.password_inp_id).send_keys(password)

    def login_submit_click(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def verify_login(self):
        act_title = self.driver.title
        if act_title == 'CredKart':
            assert True
        else:
            assert False

