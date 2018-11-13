# coding=utf-8
'''
    created on Nov.9 2018
    @author: lianghong
    description: 员工管理页面的元素与操作方法
'''

from selenium.webdriver.common.by import By
from .BasePage import BasePage
import time
from selenium.webdriver.common.keys import Keys


class StaffManagement(BasePage):
    # <----------------页面上的元素---------------->
    # 管理员模式按钮
    admin_submit = (By.XPATH, "//*[@id='app']/div/div[2]/div[1]/div[2]/button[2]")
    # 企业管理按钮
    enterprise_manage = (By.XPATH, "//*[@id='app']/div/div[1]/div/div[2]/ul/li[6]/div")
    # 员工管理按钮
    staff_management = (By.XPATH, "//*[@id='enterprise-manage$Menu']/li[4]")
    # 新增按钮
    creat_staff = (By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/button[1]")
    # 工号
    employee_id = (By.ID, "employeeID")
    # 姓名
    full_name = (By.ID, "fullName")
    # 点击公司选择框
    company = (By.CSS_SELECTOR, "div.ant-select-selection.ant-select-selection--multiple")
    # 点击取消按钮
    close_company = (By.XPATH, "//div/div[2]/div/div[1]/div[3]/div/button[1]")
    # 输入公司名
    input_company = (By.ID, "keyword")
    # 点击搜索按钮
    search_company = (By.XPATH, "//div[5]/div/div[2]/div/div[1]/div[2]/div[1]/form/div/div[2]/div/button[1]")
    # 点击清空按钮
    empty_company = (By.XPATH, "//div[5]/div/div[2]/div/div[1]/div[2]/div[1]/form/div/div[2]/div/button[2]")
    # 选择具体公司
    select_company = (By.XPATH, "//div[4]/div/div/div/div/div/table/tbody/tr[1]")
    # 点击确定按钮
    company_submit = (By.XPATH, "//div[1]/div[3]/div/button[2]")
    # 部门
    # 点击部门选择框
    department = (By.XPATH, "//form/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div/div")
    # 点击取消按钮
    close_department = (By.XPATH, "//div/div[2]/div/div[1]/div[3]/div/button[1]")
    # 输入部门编码
    input_department_code = (By.ID, "deptCode")
    # 输入部门名称
    input_department_name = (By.ID, "name")
    # 点击搜索按钮
    search_department = (By.XPATH, "//div[7]/div/div[2]/div/div[1]/div[2]/div[1]/form/div/div[2]/div/button[1]")
    # 点击清空按钮
    empty_department = (By.XPATH, "//div[7]/div/div[2]/div/div[1]/div[2]/div[1]/form/div/div[2]/div/button[2]")
    # 选择具体部门
    select_department = (By.XPATH, "//div[7]/div/div[2]/div/div[1]/div[2]/div[4]/div/div/div/div/div/table/tbody/tr[1]")
    # 点击确定按钮
    department_submit = (By.XPATH, "//div[7]/div/div[2]/div/div[1]/div[3]/div/button[2]")
    # 输入邮箱
    input_email = (By.ID, "email")
    # 点击手机号地区
    phone = (By.XPATH, "//form/div[2]/div[3]/div/div[2]/div/span/span/span/div/div/div")
    # 选择手机号地区
    select_phone = (By.CSS_SELECTOR, "li[role='menuitem'][aria-selected='false'][class='ant-select-dropdown-menu-item']")
    # 输入手机号
    input_phone = (By.ID, "mobile")
    # 选择直属领导
    leader = (By.XPATH, "//form/div[3]/div[1]/div/div[2]/div/div/div[1]/div/div/div")
    # 点击取消按钮
    close_leader = (By.XPATH, "//div/div[2]/div/div[1]/div[3]/div/button[1]")
    # 输入员工工号、姓名、手机号
    input_name_id_phone = (By.ID, "keyword")
    # 点击搜索按钮
    search_leader = (By.XPATH, "//form/div/div[2]/div/button[1]")
    # 点击清空按钮
    empty_leader = (By.XPATH, "//form/div/div[2]/div/button[2]")
    # 选择具体人员
    select_leader = (By.XPATH, "//div/div[2]/div/div[1]/div[2]/div[4]/div/div/div/div/div/table/tbody/tr[1]")
    # 点击确定按钮
    leader_submit = (By.XPATH, "//div/div[2]/div/div[1]/div[3]/div/button[2]")
    # 职务
    # 选择职务
    duty = (By.XPATH, "//form/div[3]/div[2]/div/div[2]/div/div/div[1]/div")
    # 点击取消按钮
    close_duty = (By.XPATH, "//div/div[2]/div/div[1]/div[3]/div/button[1]")
    # 输入编码从
    input_code_from = (By.ID, "codeFrom")
    # 输入编码至
    input_code_to = (By.ID, "codeTo")
    # 输入编码
    input_code = (By.ID, "value")
    # 点击搜索按钮
    search_duty = (By.XPATH, "//form/div/div[2]/div/button[1]")
    # 点击清空按钮
    empty_duty = (By.XPATH, "//form/div/div[2]/div/button[2]")
    # 选择具体人员职务
    select_duty = (By.XPATH, "//div[4]/div/div/div/div/div/table/tbody/tr[1]")
    # 点击确定按钮
    duty_submit = (By.XPATH, "//div/div[1]/div[3]/div/button[2]")
    # 职位
    # 输入职位
    input_position = (By.ID, "title")
    # 人员类型
    # 选择人员类型
    person_type = (By.XPATH, "//form/div[4]/div[1]/div/div[2]/div/div/div[1]/div/div/div")
    # 点击取消按钮
    close_person_type = (By.XPATH, "//div/div[2]/div/div[1]/div[3]/div/button[1]")
    # 输入编码从/至同职务
    # 点击搜索按钮
    search_person_type = (By.XPATH, "//form/div/div[2]/div/button[1]")
    # 点击清空按钮
    empty_person_type = (By.XPATH, "//form/div/div[2]/div/button[2]")
    # 选择具体人员类型
    select_person_type = (By.XPATH, "//div[4]/div/div/div/div/div/table/tbody/tr[1]")
    # 点击确定按钮
    person_type_submit = (By.XPATH, "//div[1]/div[3]/div/button[2]")
    # 级别
    # 选择级别
    level = (By.XPATH, "//form/div[4]/div[2]/div/div[2]/div/div/div[1]/div")
    # 点击取消按钮
    close_level = (By.XPATH, "//div/div[2]/div/div[1]/div[3]/div/button[1]")
    # 输入编码从/至同职务
    # 点击搜索按钮
    search_level = (By.XPATH, "//form/div/div[2]/div/button[1]")
    # 点击清空按钮
    empty_level = (By.XPATH, "//form/div/div[2]/div/button[2]")
    # 选择具体人员级别
    select_level = (By.XPATH, "//div[4]/div/div/div/div/div/table/tbody/tr[1]")
    # 点击确定按钮
    level_submit = (By.XPATH, "//div[1]/div[3]/div/button[2]")
    # 性别
    # 点击性别选择框
    sex = (By.XPATH, "//form/div[4]/div[3]/div/div[2]/div/div/div/div")
    # 选择性别，通过定位整个列表，通过去选择列表里面的值
    select_sex = (By.CSS_SELECTOR, ".ant-select-dropdown-menu-item")
    # 生日
    # 点击生日选择框
    birthday = (By.XPATH, "//form/div[5]/div[1]/div/div[2]/div/span/div/input")
    # 切换上一年
    birthday_last_year = (By.XPATH, "//div/div/div/div/div[2]/div[1]/div/a[1]")
    # 切换下一年
    birthday_next_year = (By.CSS_SELECTOR, ".ant-calendar-next-year-btn")
    # 切换上一月
    birthday_last_month = (By.CSS_SELECTOR, ".ant-calendar-prev-month-btn")
    # 切换下一月
    birthday_next_month = (By.CSS_SELECTOR, ".ant-calendar-next-month-btn")
    # 选择年
    birthday_year = (By.CSS_SELECTOR, ".ant-calendar-year-select")
    # 选择具体年份
    birthday_select_year = (By.XPATH,"//div[4]/div/div/div/div/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[3]/td[1]")
    # 选择月
    birthday_month = (By.CSS_SELECTOR, ".ant-calendar-month-select")
    # 选择具体月份
    birthday_select_month = (By.XPATH, "//div[4]/div/div/div/div/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[2]/td[2]")
    # 选择日
    birthday_select_day = (By.XPATH, "//div[4]/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[4]")
    # 入职时间
    # 点击入职时间选择框
    entry_time = (By.XPATH, "//form/div[5]/div[2]/div/div[2]/div/span/div/input")
    # 切换上一年
    entry_last_year = (By.XPATH, "//div/div/div/div/div[2]/div[1]/div/a[1]")
    # 切换下一年
    entry_next_year = (By.CSS_SELECTOR, ".ant-calendar-next-year-btn")
    # 切换上一月
    entry_last_month = (By.CSS_SELECTOR, ".ant-calendar-prev-month-btn")
    # 切换下一月
    entry_next_month = (By.CSS_SELECTOR, ".ant-calendar-next-month-btn")
    # 选择年
    entry_year = (By.CSS_SELECTOR, ".ant-calendar-year-select")
    # 选择具体年份
    entry_select_year = (By.XPATH, "//div[5]/div/div/div/div/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[3]/td[1]")
    # 选择月
    entry_month = (By.CSS_SELECTOR, ".ant-calendar-month-select")
    # 选择具体月份
    entry_select_month = (By.XPATH, "//div[5]/div/div/div/div/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[2]/td[2]")
    # 选择日
    entry_select_day = (By.XPATH, "//div[5]/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[4]")

    # 点击保存数据按钮
    save_submit = (By.CSS_SELECTOR, "button[type='submit']")
    # 点击取消按钮
    quit_submit = (By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div[2]/div[2]/div/form/button[2]")
    # 点击返回按钮
    back_submit = (By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/a")

    # <----------------元素操作---------------->
    def admin_submit_click(self):
        self.findElement(self.admin_submit).click()

    def enterprise_manage_click(self):
        self.findElement(self.enterprise_manage).click()

    def staff_management_click(self):
        self.findElement(self.staff_management).click()

    def create_staff_click(self):
        self.findElement(self.creat_staff).click()

    # 输入工号
    def employee_id_in(self, employee):
        self.findElement(self.employee_id).send_keys(employee)

    # 输入姓名
    def full_name_in(self, full_name):
        self.findElement(self.full_name).send_keys(full_name)

    # 选择公司
    def select_company_in(self, company_name):
        self.findElement(self.company).click()
        # self.findElement(self.close_company).click()
        # time.sleep(1)
        # self.findElement(self.company).click()
        time.sleep(1)
        self.findElement(self.input_company).send_keys(company_name)
        self.findElement(self.search_company).click()
        self.findElement(self.empty_company).click()
        self.findElement(self.select_company).click()
        time.sleep(1)
        self.findElement(self.company_submit).click()
        time.sleep(1)

    # 选择部门
    def select_department_in(self, department_code, department_name):
        self.findElement(self.department).click()
        # self.findElement(self.close_department).click()
        # time.sleep(1)
        # self.findElement(self.department).click()
        time.sleep(1)
        self.findElement(self.input_department_code).send_keys(department_code)
        self.findElement(self.input_department_name).send_keys(department_name)
        self.findElement(self.search_department).click()
        self.findElement(self.empty_department).click()
        self.findElement(self.select_department).click()
        time.sleep(1)
        self.findElement(self.department_submit).click()
        time.sleep(1)

    # 输入邮箱
    def email_in(self, email):
        self.findElement(self.input_email).send_keys(email)

    # 输入电话号码
    def phone_in(self, number):
        self.findElement(self.phone).click()
        self.findElements(self.select_phone)[0].click()
        self.findElement(self.input_phone).send_keys(number)

    # 选择直属领导
    def leader_in(self, name_id_phone):
        self.findElement(self.leader).click()
        # self.findElement(self.close_leader).click()
        # time.sleep(1)
        # self.findElement(self.leader).click()
        time.sleep(3)
        self.findElement(self.input_name_id_phone).send_keys(name_id_phone)
        self.findElement(self.search_leader).click()
        self.findElement(self.empty_leader).click()
        self.findElement(self.select_leader).click()
        time.sleep(1)
        self.findElement(self.leader_submit).click()

    # 选择职务
    def duty_in(self, code_from, code_to, code):
        self.findElement(self.duty).click()
        # self.findElement(self.close_duty).click()
        # time.sleep(1)
        # self.findElement(self.duty).click()
        time.sleep(1)
        self.findElement(self.input_code_from).send_keys(code_from)
        self.findElement(self.input_code_to).send_keys(code_to)
        self.findElement(self.input_code).send_keys(code)
        self.findElement(self.search_duty).click()
        self.findElement(self.empty_duty).click()
        time.sleep(1)
        self.findElement(self.select_duty).click()
        self.findElement(self.duty_submit).click()

    # 输入职位
    def position_in(self, position):
        self.findElement(self.input_position).send_keys(position)

    # 选择人员类型
    def person_type_in(self, person_type_code_from, person_type_code_to, person_type_code):
        self.findElement(self.person_type).click()
        # self.findElement(self.close_person_type).click()
        # time.sleep(1)
        # self.findElement(self.person_type).click()
        time.sleep(1)
        self.findElement(self.input_code_from).send_keys(person_type_code_from)
        self.findElement(self.input_code_to).send_keys(person_type_code_to)
        self.findElement(self.input_code).send_keys(person_type_code)
        self.findElement(self.search_person_type).click()
        self.findElement(self.close_person_type).click()
        time.sleep(1)
        self.findElement(self.select_person_type).click()
        self.findElement(self.person_type_submit).click()

    # 选择级别
    def level_in(self, level_code_from, level_code_to, level_code):
        self.findElement(self.level).click()
        # self.findElement(self.close_level).click()
        # time.sleep(1)
        # self.findElement(self.level).click()
        time.sleep(1)
        self.findElement(self.input_code_from).send_keys(level_code_from)
        self.findElement(self.input_code_to).send_keys(level_code_to)
        self.findElement(self.input_code).send_keys(level_code)
        self.findElement(self.search_level).click()
        self.findElement(self.close_level).click()
        time.sleep(1)
        self.findElement(self.select_level).click()
        self.findElement(self.leader_submit).click()

    # 选择性别
    def sex_in(self):
        self.findElement(self.sex).click()
        self.findElements(self.select_sex)[1].click()

    # 下拉
    def switch_to(self):
        self.findElement(self.birthday).sendKeys(Keys.DOWN)
        time.sleep(1)
        self.findElement(self.birthday).sendKeys(Keys.DOWN)
        time.sleep(1)
        self.findElement(self.birthday).sendKeys(Keys.DOWN)
        time.sleep(1)
        self.findElement(self.birthday).sendKeys(Keys.DOWN)
        time.sleep(1)

    # 选择生日时间
    def birthday_in(self):
        # self.findElement(self.birthday).click()
        self.findElement(self.birthday_last_year).click()
        self.findElement(self.birthday_next_year).click()
        self.findElement(self.birthday_last_month).click()
        self.findElement(self.birthday_next_month).click()
        self.findElement(self.birthday_year).click()
        self.findElement(self.birthday_select_year).click()
        self.findElement(self.birthday_month).click()
        self.findElement(self.birthday_select_month).click()
        self.findElement(self.birthday_select_day).click()

    # 选择入职时间
    def entry_time_in(self):
        self.findElement(self.entry_time).click()
        self.findElement(self.entry_last_year).click()
        self.findElement(self.entry_next_year).click()
        self.findElement(self.entry_last_month).click()
        self.findElement(self.entry_next_month).click()
        self.findElement(self.entry_year).click()
        self.findElement(self.entry_select_year).click()
        self.findElement(self.entry_month).click()
        self.findElement(self.entry_select_month).click()
        self.findElement(self.entry_select_day).click()

    # 保存数据
    def save_submit_in(self):
        self.findElement(self.save_submit).click()

    # 取消
    def quit_in(self):
        self.findElement(self.quit_submit).click()

    # 返回
    def back_in(self):
        self.findElement(self.back_submit).click()

    # 进入员工管理页面步骤
    def click_staff(self):
        self.admin_submit_click()
        self.enterprise_manage_click()
        self.staff_management_click()

    # 新建人员步骤
    def create_staff(self, employee_id, full_name, company_name, department_code, department_name, email,
                     number, name_id_phone, duty_code_from, duty_code_to, duty_code, position, person_type_from,
                     person_type_to, person_code, level_code_from, level_code_to, level_code):
        self.create_staff_click()
        self.employee_id_in(employee_id)
        self.full_name_in(full_name)
        self.select_company_in(company_name)
        self.select_department_in(department_code, department_name)
        self.email_in(email)
        # self.phone_in(number)
        # self.leader_in(name_id_phone)
        # self.duty_in(duty_code_from, duty_code_to, duty_code)
        # self.position_in(position)
        # self.person_type_in(person_type_from, person_type_to, person_code)
        # self.level_in(level_code_from, level_code_to, level_code)
        # self.sex_in()
        # self.switch_to()
        # self.birthday_in()
        # self.entry_time_in()
        self.save_submit_in()
        # self.quit_in()
        # self.back_in()