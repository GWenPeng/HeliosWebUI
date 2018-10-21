from selenium import webdriver
import unittest
from  pages.LoginPage.LoginPage import *

def test_Login_success():
    lg= LoginPage(seleniumDriver='..\\Drivers\\chromedriver.exe',baseUrl="https://console.huilianyi.com/#/login")
    lg.open()
    lg.login('13323454321','hly123')








