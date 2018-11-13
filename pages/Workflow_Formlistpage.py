# coding=utf-8
'''
    created on Nov.9 2018
    @author: yuxiong
    description: 审批流页面的元素与操作方法
'''

from selenium.webdriver.common.by import By
from .BasePage import BasePage


class Workflow_Formlistpage(BasePage):
    # <----------------页面上的元素---------------->
    # 管理员模式按钮
    admin_button = (By.XPATH, "//*[@id='app']/div/div[2]/div[1]/div[2]/button[2]")
    # 切换公司模式按钮
    company_model = (By.XPATH, "/html/body/div[4]/div/div/ul/li[2]")
    # 确认按钮
    confirm_button = (By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div[3]/div/button[2]")
    # 设置按钮
    set_button = (By.XPATH, "//*[@id='app']/div/div[1]/div/div[2]/ul/li[1]/div/span/span")
    # 审批流按钮
    workflow_button = (By.XPATH, "//*[@id='setting$Menu']/li[19]/div")
    # 启用按钮
    Enable_button = (By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div/div/div/div[1]/label[1]/span[2]")
    # 禁用按钮
    Disable_button = (By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div/div/div/div[1]/label[2]/span[2]")
    # 查看编辑按钮
    Edit_button = (By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/a")
    # 复制按钮
    copy_button = (By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div/a")
    # 粘贴按钮
    paste_submit = (By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div/a[2]")
    # 审批流文本
    workflowtitle = (By.XPATH, "//*[@id='app'']/div/div[2]/div[1]/div[3]/span[2]/span[1]")
    # < ----------------页面上的元素 - --------------->


    # < ----------------元素的操作 - --------------->
    # 点击管理员模式按钮
    def Click_adminbutton(self):
        self.findElement(self.admin_button).click()
    # 点击切换公司模式按钮
    def Click_company_modelbutton(self):
        self.findElement(self.company_model).click()
    # 点击确认按钮
    def Click_confirmbutton(self):
        self.findElement(self.confirm_button).click()
    # 点击设置按钮
    def Click_setbutton(self):
        self.findElement(self.set_button).click()
    # 点击审批流按钮
    def Click_workflowbutton(self):
        self.findElement(self.workflow_button).click()
    # 点击启用按钮
    def Click_Enablebutton(self):
        self.findElement(self.Enable_button).click()
    # 点击禁用按钮
    def Click_Disablebutton(self):
        self.findElement(self.Disable_button).click()
    # 点击查看编辑按钮
    def Click_editbutton(self):
        self.findElement(self.Edit_button).click()
    # 点击复制按钮
    def Click_copybutton(self):
        self.findElement(self.copy_button).click()
    # 点击粘贴按钮
    def Click_pastebutton(self):
        self.findElement(self.paste_submit).click()
    # 获取页面标志
    def workflowtitle(self):
        workflowtitle = self.findElement(self.workflowtitle).text
        return workflowtitle
    # < ----------------元素的操作 - --------------->

    # < ----------------用例通用步骤 - --------------->
        # 进入审批流的组合方法
    def Enter_workflow(self):
            self.Click_adminbutton()
            self.Click_company_modelbutton()
            self.Click_confirmbutton()
            self.Click_setbutton()
            self.Click_workflowbutton()
    # < ----------------用例通用步骤 - --------------->