import unittest
from  pages.LoginPage import LoginPage
from  testcases.DefaultTest import DefaulTest
from common.loggen import Logger
class TestLogin(DefaulTest):
   def test_Login_success(self):
            lg=LoginPage()
            lg.open()
            lg.login('13323454321','hly123')
            Logger("日志文件").getlog().info('登陆成功')















