import unittest
import  common.mainModule
from selenium import  webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging

module_logger = logging.getLogger("mainModule.DefaultTest")
class DefaulTest(unittest.TestCase):
    # logger = logging.getLogger("mainModule.sub.Default")
    # logger.info("creating an instance in SubModuleClass")
    @classmethod
    def setUpClass(cls):

        # cls.driver = webdriver.Chrome()
        #使用本地driver
        cls.driver=webdriver.Remote(command_executor='http://47.100.188.71:4444/wd/hub',
             desired_capabilities=DesiredCapabilities.CHROME)
        #调用远程selenium grid的driver
        # opt=webdriver.Chrome.create_options().add_argument('start-maximized')
        cls.url="https://console.huilianyi.com/#/login"
        cls.driver.implicitly_wait(30)
        #chrom需要注销掉
        #
        cls.driver.set_window_size(width="1920", height="1080")
        # cls.driver.maximize_window() 窗口最大化
        # rect = cls.driver.get_window_size()
        # print(rect)
        # logger = logging.getLogger("mainModule.sub.module")
        module_logger.info('Start Testing')
    @classmethod
    def tearDownClass(cls):
         cls.driver.quit()
         module_logger.info('End Testing')





