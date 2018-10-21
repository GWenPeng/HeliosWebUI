# code=utf-8

'''
created on Sep.28 2018
@author: chuanlin
description: 中控登录页面的元素与操作方法
'''

from selenium.webdriver.common.by import By
from BasePage import BasePage


class LoginPage(BasePage):

    # #############页面上的元素######################
    # 登录框
    username_loc = (By.CSS_SELECTOR, "input[type='text']")
    # 密码框
    password_loc = (By.CSS_SELECTOR, "input[type='password']")
    # 登录按钮
    loginButton_loc = (By.CSS_SELECTOR, "button[type='button']")

    # 企业登录跳转按钮
    companyLogin_loc = (By.XPATH, "//*[@id='app']/div/div[1]/div[2]/div[1]/div/div/div[1]")
    # 普通登录跳转按钮（点击企业登录后出现）
    normalLogin_loc = (By.XPATH, "//*[@id='app']/div/div[1]/div[2]/div[1]/div/div/div/div[1]")
    # 找回密码按钮
    forgetPassword_loc = (By.XPATH, "//*[@id='app']/div/div[1]/div[2]/div[1]/div/div/div[2]")
    # 返回登录按钮（点击忘记密码之后出现）
    backToLogin_loc = (By.XPATH, "//*[@id='app']/div/div[1]/div[3]/div[2]/a")
    # 企业登陆账号输入框
    companyLoginUsername_loc = (By.XPATH, "//*[@id='app']/div/div[1]/div[2]/div[1]/div/div/input")
    # 企业登陆的下一步按钮
    nextStep_loc = (By.XPATH, "//*[@id='app']/div/div[1]/div[2]/div[1]/div/div/button")

    # #####################元素操作###########################
    # 输入用户名
    def input_username(self, username):
        self.findElement(self.username_loc).clear()
        self.findElement(self.username_loc).send_keys(username)

    # 输入密码
    def input_password(self, password):
        self.findElement(self.password_loc).send_keys(password)

    # 点击登录按钮
    def submit(self):
        self.findElement(self.loginButton_loc).click()

    # 普通登录组合方法
    def login(self, username, password):
        self.open()
        self.input_username(username)
        self.input_password(password)
        self.click_loginButton()

    # 打开网页
    def open(self):
        self._open(self.baseUrl)