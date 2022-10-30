from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname)__file__),"..",".."))
from POMdemo.pages.loginpage import Loginpage
from POMdemo.pages.homepage import Homepage
import HTMLTestRunner



class LoginTest(unittest.TestCase) :
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Users/testeur/PycharmProjects/test/drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = Loginpage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_botton_login()
        homepage=Homepage(driver)
        homepage.welcome_list()
        homepage.logout_button()
        #self.driver.find_element_by_xpath('//input[@name="username"]').send_keys("Admin")
        #self.driver.find_element_by_xpath('//*[@name="password"]').send_keys("admin123")
        #self.driver.find_element_by_xpath('//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]').click()
        #self.driver.find_element_by_xpath('//i[@class="oxd-icon bi-caret-down-fill oxd-userdropdown-icon"]').click()
        #time.sleep(5)
        #self.driver.find_element_by_xpath('//*[@href="/web/index.php/auth/logout"]').click()
        #time.sleep(5)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunnner(output='C:/Users/testeur/PycharmProjects/test/reports'))






