# coding = utf-8

'''
created on Sep.21 2018
@author: chuanlin
description: 基类页面，封装其他所有页面所用到的公用属性和方法
'''


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import  ActionChains
class BasePage(object):

    def __init__(self,seleniumDriver, baseUrl="https://console.huilianyi.com/#/login"):
        #初始化驱动或baseURL
        self.driver = seleniumDriver
        self.baseUrl = baseUrl



    # 通过title断言进入的页面是否正确
    def check_page_title(self, pageTitle):
        return pageTitle in self.driver.title()

    # 打开页面，并校验页面链接是否加载正确
    def _open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

        # assert self.checkPageTitle(pageTitle), u"打开页面失败 %s"%url

    # 定义open方法，调用_open()进行打开链接
    def open(self):
        self._open(self.baseUrl)

    def browser_quit(self):
        self.driver.quit()

    # 定位页面元素的方法
    def findElement(self, loc):
        try:
            WebDriverWait(self.driver, 100).until(ec.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("未找到元素")

    # 封装send_keys方法
    def sendKeys(self, loc, value, locateFirst=False, clearFirst=False):
        try:
            loc = getattr(self, "_%s"%loc)
            if locateFirst:
                self.findElement(*loc).click()
            if clearFirst:
                self.findElement(*loc).clear()

            self.findElement(*loc).send_keys(value)
        except AttributeError:
            print ("页面中未找到元素")

    # 重写switch_frame方法
    def switchFrame(self, loc):
        return self.driver.switch_to_frame(loc)

    # 定义script方法，用于执行js脚本，返回执行结果
    def script(self, src):
        self.driver.execute_script(src)


    #<------------------以下是鼠标通用方法------------------------>
    def hovering(self,to_element):
        # 鼠标悬停
        """
                Moving the mouse to the middle of an element.

                :Args:
                 - to_element: The WebElement to move to.
        """
        mouse=ActionChains(driver=self.driver)
        mouse.move_to_element(to_element).perform()

    #< ------------------以下是鼠标通用方法 - ----------------------->