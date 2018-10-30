import unittest
from  pages.LoginPage import LoginPage
# from  testcases.DefaultTest import DefaulTest
from selenium import webdriver
from common.loggen import Logger
class TestLogin(unittest.TestCase):
   def setUp(self):
       self.driver=webdriver.Chrome()
       self.url="https://console.huilianyi.com/#/login"
       self.username = "13323454321"
       self.password = "hly123"

   def test_Login_success(self):
            lg=LoginPage(seleniumDriver=self.driver,baseUrl=self.url)
            lg.login(self.username,self.password)
            Logger("日志文件").getlog().info('登陆成功')

   def tearDown(self):
       self.driver.quit()
















