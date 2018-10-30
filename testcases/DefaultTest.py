import unittest
from common.loggen import Logger
from selenium import  webdriver
class DefaulTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome()
        cls.url="https://console.huilianyi.com/#/login"
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # cls.driver.get('https://console.huilianyi.com/#/login')
        Logger("日志文件").getlog().info('Start Testing')

    @classmethod
    def tearDownClass(cls):
         cls.driver.quit()
         Logger("日志文件").getlog().info('End Testing')





