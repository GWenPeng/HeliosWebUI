from  pages.LoginPage import LoginPage
from  testcases.DefaultTest import DefaulTest
import  common.mainModule
import logging
module_logger = logging.getLogger("mainModule.DefaultTest.Testlogin")
class TestLogin(DefaulTest):

   def test_Login_success(self):
            lg=LoginPage(seleniumDriver=self.driver,baseUrl=self.url)
            lg.login( "13323454321","hly123")
            module_logger.info('登陆成功')

















