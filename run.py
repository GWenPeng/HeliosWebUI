
from scripts import *
import  time
import os.path
import unittest
import common.HTMLTestRunner
from common.loggen import Logger
import logging

class Runner(unittest.TestCase):
    def setUp(self):
        print('start testing测试执行')

    def test_helios(self):
        tspath=os.path.abspath('.')
        tsname=tspath+'\\data\\testsuite.xlsx'
        self.assertTrue(read_testsuite(tsname))

    def tearDown(self):
        print('end testing测试执行')


if __name__ == '__main__':
    test=unittest.TestSuite()
    test.addTest(Runner('test_helios'))
    rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    file_path=os.path.abspath('.')+'\\report\\'+rq+'-result.html'
    file_result=open(file_path,'wb')

    Logger('日志文件').getlog().info('测试完成，正在生成测试报告')
    running=common.HTMLTestRunner.HTMLTestRunner(stream=file_result,title=u'helios测试报告',description=u'用例执行情况')
    running.run(test)
    file_result.close()