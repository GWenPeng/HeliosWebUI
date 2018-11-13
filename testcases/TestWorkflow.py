from pages.LoginPage import LoginPage
from pages.Workflow_Formlistpage import Workflow_Formlistpage
from testcases.DefaultTest import DefaulTest
import time
import  common.mainModule
import logging
module_logger = logging.getLogger("mainModule.DefaultTest.Testlogin")
class Testworkflow(DefaulTest):
    def test_workflow_success(self):
            wf = LoginPage(seleniumDriver=self.driver, baseUrl=self.url)
            wf.login("18601687603", "hly123")
            wf = Workflow_Formlistpage(seleniumDriver=self.driver, baseUrl=self.url)
            wf.Enter_workflow()
            self.assertEquals("审批流", wf.workflowtitle(), msg="进入审批流失败")
            module_logger.info('进入审批流列表页成功')
            wf.Click_editbutton()
            module_logger.info('进入审批流详情页')
if __name__ == '__main__':
    Testworkflow()
