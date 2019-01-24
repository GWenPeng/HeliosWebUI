from pages.StaffManagementPage import StaffManagement
from  testcases.DefaultTest import DefaulTest
from  pages.LoginPage import LoginPage
# import  time
import common.mainModule
import logging
import  unittest
module_logger = logging.getLogger("mainModule.DefaultTest.TestCreateStaff")

class TestCreateStaff(DefaulTest):
   def test_create_staff_success(self):

        lg = LoginPage(seleniumDriver=self.driver, baseUrl=self.url)
        lg.login("15773250001", "hly123")
        cs = StaffManagement(seleniumDriver=self.driver, baseUrl=self.url)
        # time.sleep(4)
        cs.click_staff()
        module_logger.info("进入到员工管理页面")
        cs.create_staff("1109003", "自动化测试新增3", "stage", "1", "stage测试", "1109003@sina.com",
                        "55556666", "stage", "1", "2", "2", "自动化测试", "2", "3", "3", "3", "4", "4")
        module_logger.info("员工新增成功")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestCreateStaff('test_create_staff_success'))
    # suite.run(testsuite)
    runner = unittest.TextTestRunner(verbosity=2) #// 详细模式
    runner.run(suite)