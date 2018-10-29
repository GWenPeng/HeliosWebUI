
from scripts import *
import  time
import os.path
import unittest
import common.HTMLTestRunner
from common.loggen import Logger
import unittest
from Email.send_email import Send_email_Attachment
from unittest import TestLoader

from testcases.TestLogin import TestLogin
import logging

# class Runner(unittest.TestCase):
#     def setUp(self):
#         print('start testing测试执行')
#
#     def test_helios(self):
#         tspath=os.path.abspath('.')
#         tsname=tspath+'\\data\\testsuite.xlsx'
#         self.assertTrue(read_testsuite(tsname))
#
#     def tearDown(self):
#         print('end testing测试执行')


if __name__ == '__main__':
    suite=unittest.TestSuite()
    """
     suite = unittest.TestSuite()
 　　suite.addTest(TestLogin('test_Login_success'))
 　　suite.run(testsuite)
     runner = unittest.TextTestRunner(verbosity=2) //详细模式
　　 runner.run(suite)
     //执行测试用例集
    """
    # loader = TestLoader()
    # loader.testMethodPrefix = 'test'
    # 添加并执行测试类
    discover=unittest.defaultTestLoader.discover(start_dir="./testcases",pattern="Test*.py",top_level_dir=None)
    rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    file_path=os.path.abspath('.')+'\\report\\'+rq+'-result.html'
    file_result=open(file_path,'wb')

    Logger('日志文件').getlog().info('测试完成，正在生成测试报告')
    running=common.HTMLTestRunner.HTMLTestRunner(stream=file_result,title=u'helios测试报告',verbosity=2,description=u'用例执行情况')

    running.run(discover)
    file_result.close()
    Send_email_Attachment(sendfile=file_path, ).Send_email()