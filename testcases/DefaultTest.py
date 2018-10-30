import unittest
from common.loggen import Logger
from  pages.BasePage import  BasePage
class DefaulTest(unittest.TestCase):
    def setUp(self):
        Logger("日志文件").getlog().info('Start Testing')


    def tearDown(self):
         BasePage().browser_quit()
         Logger("日志文件").getlog().info('End Testing')





