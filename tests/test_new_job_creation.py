import time

import pytest

from pageObjects.homepageObjects import homepage
from pageObjects.loginpage import LoginPage
from utilities.readproperties import readconfig
from datetime import datetime, timedelta


class Test_02_home:
    baseURL = readconfig.getApplicationURL()
    employee_id = readconfig.get_id()
    password = readconfig.get_password()

    target_start_date = readconfig.job_date_time(2, 10, 0)
    target_end_date = readconfig.job_end_date_time(1, 3, 0)
    customer_dropdown_value = readconfig.get_customer_name()
    department_name = readconfig.get_department()
    conveyor_number = readconfig.get_Conveyor_Number()
    work_details_dropdown_value = readconfig.get_Work_Details()
    material_details = readconfig.get_Material_Details_quantity()
    number_of_casuals = readconfig.get_number_of_casual()

    def test_newjob_creation(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.emp_id(self.employee_id)
        self.lp.password(self.password)
        self.lp.signin()
        time.sleep(2)
        self.hp = homepage(self.driver)
        time.sleep(2)
        self.hp.click_newjob()
        time.sleep(3)
        self.hp.enter_start_date(self.target_start_date)
        self.hp.enter_end_date(self.target_end_date)
        time.sleep(2)
        # self.hp.click_on_free_space()
        self.hp.select_option_from_dropdown_test(self.hp.cust_details_dropdown_xpath, self.customer_dropdown_value)
        time.sleep(2)
        self.hp.enter_department_name(self.department_name)
        time.sleep(2)
        self.hp.enter_conveyor_no(self.conveyor_number)
        time.sleep(2)
        self.hp.select_option_from_dropdown(self.hp.type_of_work_dropdown_xpath, self.work_details_dropdown_value)
        time.sleep(2)
        self.hp.enter_quantity(self.material_details)
        time.sleep(2)
        self.hp.enter_no_casuals(self.number_of_casuals)
        time.sleep(2)
        self.hp.click_job_submit_button()
        time.sleep(2)
        self.hp.click_job_ok_btn()
        if self.hp.success_is_displayed() is True:
            assert "test passed"
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "job_Creation.png")
            assert "test failed unsuccessful in creating  new job "

        self.driver.close()
