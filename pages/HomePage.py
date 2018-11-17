# code=utf-8

'''
created on Sep.28 2018
@author: guwenpeng
description: 登陆成功的首页
'''

from selenium.webdriver.common.by import By
from .BasePage import BasePage
#from api.Get_Oauth_Token_Api import GetOauthTokenApi
from api.Get_Enble_Expense_FormLists_Api import Get_Enble_Expense_FormLists_Api

class HomePage(BasePage):
    # def __init__(self,seleniumDriver, baseUrl=""):
    #     self.driver=super
    #     pass
    # <----------------以下为页面上element---------------->
    Dashboard= (By.CSS_SELECTOR, "#app > div > div.helios-sider.ant-layout-sider > div > div.menu-container > ul > li.ant-menu-item.ant-menu-item-selected > div")
    #仪表盘 element
    Expense_Report=(By.XPATH,"//*[@id='app']/div/div[1]/div/div[2]/ul/li[3]/div")
    #报销单 element
    My_Expense_Claim = (By.CSS_SELECTOR,"#expense-parent-report\\24 Menu > li")
    # 我的报销单 element
    New_Expense_Report=(By.CSS_SELECTOR,'#app > div > div.content-layout.ant-layout > div.helios-content.ant-layout-content > div > div.table-header > div.table-header-buttons > button')
    # 新建报销单 element
    Group_Mode =(By.CSS_SELECTOR,'#app > div > div.helios-sider.ant-layout-sider > div > div.company-name > span')
    #集团模式 element
    Change_Company =(By.CSS_SELECTOR,'body > div:nth-child(10) > div > div > ul > li')
    #切换公司模式 element
    Change_Gruop =(By.CSS_SELECTOR,'body > div:nth-child(10) > div > div > ul > li:nth-child(1)')
    #切换集团模式 element
    Toast_Submit=(By.CSS_SELECTOR,'body > div:nth-child(11) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > button.ant-btn.ant-btn-primary')
    #切换集团公司的弹窗确认按钮 element
    Application =(By.CSS_SELECTOR,'#app > div > div.helios-sider.ant-layout-sider > div > div.menu-container > ul > li:nth-child(4) > div')
    #申请单 element

    # <----------------以下为页面上element--------------->
    # |
    # |
    # |
    # |
    # < ----------------以下为元素操作 ----------------->
    def click_expense_report(self):
        #点击报销
        self.findElement(self.Expense_Report).click()

    def click_my_Expense_claim(self):
        # 点击我的报销单
        self.findElement(self.My_Expense_Claim).click()

    def move_to_new_expense_report(self):
        #移动鼠标至新建报销单
        el=self.findElement(self.New_Expense_Report)
        self.hovering(el)

    def click_group_mode(self):
        #点击集团模式
        self.findElement(self.Group_Mode).click()

    def click_change_company(self):
        #点击切换公司
        self.findElement(self.Change_Company).click()

    def click_toast_submit(self):
        #切换集团公司的弹窗确认按钮
        self.findElement(self.Toast_Submit).click()

    def click_application(self):
        #点击申请单
        self.findElement(self.Application).click()

    def find_daily_expense_report(self,index):

        pass

# < ----------------以上为元素操作 ----------------->


