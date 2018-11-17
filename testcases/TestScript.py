import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.ApplicationPage import ApplicationPage
from testcases.DefaultTest import DefaulTest


class TestScript(DefaulTest):


    def test_script(self):
        # self.driver = webdriver.Chrome("C:\\Program Files (x86)\\Java\\jdk1.8.0_171\\bin\\chromedriver.exe")

        lg = LoginPage(seleniumDriver=self.driver, baseUrl='http://uat.huilianyi.com')
        lg.login('18323454321','hly123')
        hp = HomePage(seleniumDriver=self.driver, baseUrl='http://uat.huilianyi.com')
        hp.click_group_mode()
        hp.click_change_company()
        sleep(1)
        hp.click_toast_submit()
        sleep(1)
        hp.click_application()
        sleep(1)
        ap=ApplicationPage(seleniumDriver=self.driver, baseUrl='http://uat.huilianyi.com')
        ap.creat_application_form()
        sleep(3)




if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestScript('test_script'))
    # suite.run(testsuite)
    runner = unittest.TextTestRunner(verbosity=2)  # // 详细模式
    runner.run(suite)