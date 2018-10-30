import unittest
from common.loggen import Logger
from  pages.BasePage import  BasePage
class DefaulTest():
    # bp=BasePage(seleniumDriver='.\\Drivers\\chromedriver.exe', baseUrl="https://console.huilianyi.com/#/login")
    def setUp(self):
        # self.bp.open()
        Logger("日志文件").getlog().info('Start Testing')


    def tearDown(self):
         BasePage().browser_quit()
         Logger("日志文件").getlog().info('End Testing')





