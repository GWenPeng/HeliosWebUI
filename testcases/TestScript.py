import unittest
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage

from testcases.DefaultTest import DefaulTest


class TestScript(DefaulTest):


    def test_script(self):
        lg = LoginPage(seleniumDriver=self.driver, baseUrl='http://uat.huilianyi.com')
        lg.login('18323454321','hly123')
        hp = HomePage(seleniumDriver=self.driver, baseUrl='http://uat.huilianyi.com')
        hp.click_group_mode()
        hp.click_change_company()





if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestScript('test_script'))
    runner = unittest.TextTestRunner(verbosity=2)  # // 详细模式
    runner.run(suite)