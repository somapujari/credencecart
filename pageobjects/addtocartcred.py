from selenium.webdriver.common.by import By


class AddToCart:
    applemack_lnk_xpath = "//h3[contains(text(),'Apple Macbook Pro')]"
    addcart_btn_xpath = '//input[@value="Add to Cart"]'
    text_verify_xpath = '//div[@class="alert alert-success"]'

    def __init__(self, driver):
        self.driver = driver

    def macbook_click(self):
        self.driver.find_element(By.XPATH, self.applemack_lnk_xpath).click()

    def add_to_cart_click(self):
        self.driver.find_element(By.XPATH,self.addcart_btn_xpath).click()

    def verify_ass_to_cart(self):
        tex = self.driver.find_element(By.XPATH, self.text_verify_xpath).text
        if tex == 'Item was added to your cart!':
            assert True
        else:
            assert False







