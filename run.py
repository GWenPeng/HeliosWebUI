
# from scripts import *
import  time
import os.path
# import unittest
import common.HTMLTestRunner
import  common.mainModule
import unittest
from Email.send_email import Send_email_Attachment
import  logging
module_logger=logging.getLogger('mainModule.run')
#     def test_helios(self):
#         tspath=os.path.abspath('.')
#         tsname=tspath+'\\data\\testsuite.xlsx'
#         self.assertTrue(read_testsuite(tsname))

if __name__ == '__main__':
    # suite=unittest.TestSuite()
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

    try:
        running=common.HTMLTestRunner.HTMLTestRunner(stream=file_result,title=u'helios测试报告',verbosity=2,description=u'用例执行情况')
        running.run(discover)
        file_result.close()

    except Exception as e:
        module_logger.info('测试报告生成失败')
    else:
        module_logger.info('测试报告生成成功')
        module_logger.info('邮件正在发送')
        Send_email_Attachment(sendfile=file_path, ).Send_email()


