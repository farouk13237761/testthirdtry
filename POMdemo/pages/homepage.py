from POMdemo.locators.locator import Locators
class Homepage():


    def __int__(self,driver):
        self.driver=driver
        self.welcome_menu_xpath=Locators.welcome_menu_xpath
        self.logout_xpath=Locators.logout_xpath


    def welcome_list(self):
        self.driver.find_element_by_xpath('Locators.welcome_menu_xpath').click()

    def logout_button(self):
        self.driver.find_element_by_xpath('Locators.logout_xpath').click()
