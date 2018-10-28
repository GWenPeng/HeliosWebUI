
import unittest



class DefaulTest(unittest.TestCase):
    def setUp(self):
        print('Start Testing测试开始')


    def tearDown(self):
        # self.driver.quit()
        print('End Testing测试完成')




def test_Login_success(self, lg):
    lg.open()
    lg.login('13323454321', 'hly123')
