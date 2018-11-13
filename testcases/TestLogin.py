from  pages.LoginPage import LoginPage
from  testcases.DefaultTest import DefaulTest
import  common.mainModule
import logging
module_logger = logging.getLogger("mainModule.DefaultTest.Testlogin")
class TestLogin(DefaulTest):
     def test_Login_success(self):
        # try:
               lg = LoginPage(seleniumDriver=self.driver, baseUrl=self.url)
               lg.login("13323454321", "hly123")
               # time.sleep(3)
               # self.assertEquals("一壶清酒stage", lg.user_name_in(), msg="登录失败！！")
               module_logger.info('登录成功')
        # except :
        #      module_logger.exception("登陆失败", exc_info=True)
        #      return  False
