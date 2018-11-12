from pages.StaffManagementPage import StaffManagement
from testcases.TestLogin import TestLogin
import common.mainModule
import time
import logging
module_logger = logging.getLogger("mainModule.DefaultTest.TestCreateStaff")

class TestLogin(TestLogin):
   def test_create_staff_success(self):
        cs = StaffManagement(seleniumDriver=self.driver, baseUrl=self.url)
        cs.click_staff()
        module_logger.info("进入到员工管理页面")
        cs.create_staff("1109003", "自动化测试新增3", "stage", "1", "stage测试", "1109003@sina.com",
                        "55556666", "stage", "1", "2", "2", "自动化测试", "2", "3", "3", "3", "4", "4")
        module_logger.info("员工新增成功")