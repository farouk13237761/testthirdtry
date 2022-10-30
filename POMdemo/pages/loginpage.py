from POMdemo.locators.locator import Locators
class Loginpage ():

    def __int__(self,driver):
        self.driver=driver
        self.username_textbox_xpath=Locators.username_textbox_xpath
        self.password_textbox_xpath=Locators.password_textbox_xpath
        self.login_botton_xpath=Locators.login_botton_xpath
    def enter_username(self,username):
        self.driver.find_element_by_xpath('Locators.username_textbox_xpath').clear()
        self.driver.find_element_by_xpath('Locators.username_textbox_xpath').send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_xpath('').clear()
        self.driver.find_element_by_xpath('self.password_textbox_xpath').send_keys(password)
    def click_botton_login(self):
        self.driver.find_element_by_xpath('self.login_botton_xpath').click()










