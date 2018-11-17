# code=utf-8
from time import sleep

from selenium.webdriver.common.by import By
from .BasePage import BasePage

class ApplicationPage(BasePage):

    # <----------------以下为页面上element---------------->
    creat_application=(By.CSS_SELECTOR,'#app > div > div.content-layout.ant-layout > div.helios-content.ant-layout-content > div > div.table-header > div.table-header-buttons > button')
    # 新建申请单 element


    # <----------------以上为页面上element--------------->

    def move_creat_application(self):
        #移动到新建申请单
        el=self.findElement(self.creat_application)
        self.hovering(el)

    #组合操作：移动到新建申请单并点击第一个单据
    def creat_application_form(self):
        el = self.findElement(self.creat_application)
        self.hovering(el)
        #创建第一个申请单表单
        list = self.driver.find_elements_by_css_selector('body > div:nth-child(12) > div > div > ul > li')
        # print(len(a))  输出有多少个元素
        list[0].click()

