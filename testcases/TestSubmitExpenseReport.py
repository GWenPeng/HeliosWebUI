from  pages.LoginPage import LoginPage
from  testcases.DefaultTest import DefaulTest
import  common.mainModule
import logging
module_logger = logging.getLogger("mainModule.DefaultTest.Testlogin")
class TestSubmitExpenseReport(DefaulTest):
    def test_submit_success(self):

        module_logger.info('报销单创建成功')
        pass