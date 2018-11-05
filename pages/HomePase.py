# code=utf-8

'''
created on Sep.28 2018
@author: guwenpeng
description: 登陆成功的首页
'''
from selenium.webdriver.common.by import By
from .BasePage import BasePage
from api.Get_Oauth_Token_Api import GetOauthTokenApi
from  api.Expense_Report_Type import Expense_Report_Type
from api.Get_Enble_Expense_FormLists_Api import Get_Enble_Expense_FormLists_Api

class HomePage(BasePage):
    # <----------------以下为页面上element---------------->
    Dashboard= (By.CSS_SELECTOR, "#app > div > div.helios-sider.ant-layout-sider > div > div.menu-container > ul > li.ant-menu-item.ant-menu-item-selected > div")
    #仪表盘 element
    Expense_Report=(By.CSS_SELECTOR, "#app > div > div.helios-sider.ant-layout-sider > div > div.menu-container > ul > li.ant-menu-submenu.ant-menu-submenu-inline.ant-menu-submenu-open > div > span > span")
    #报销单 element
    My_Expense_Claim = (By.CSS_SELECTOR,'#expense-parent-report\24 Menu > li > div')
    # 我的报销单 element
    New_Expense_Report=(By.CSS_SELECTOR,'//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div[2]/button')
    # 新建报销单 element
    Expense_Report_Lists=(By.CSS_SELECTOR,"body > div:nth-child(11) > div > div > ul")
    #新建的报销单列表元素

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
        self.hovering(self.New_Expense_Report)

    def find_daily_expense_report_element(self,num):
        access_token = GetOauthTokenApi(username="19902132186", password="a11111").get_access_token()
        num_report_name = Get_Enble_Expense_FormLists_Api(access_token=access_token).get_expense_claim_name(num=num,reportType=Expense_Report_Type.daily_report_type.value)
        el=self.findElements(self.Expense_Report_Lists)

        print(self.findElements(self.Expense_Report_Lists))

        pass

# < ----------------以上为元素操作 ----------------->
