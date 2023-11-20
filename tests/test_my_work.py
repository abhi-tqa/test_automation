import time

import pytest

from pageObjects.homepageObjects import homepage
from pageObjects.loginpage import LoginPage
from utilities.readproperties import readconfig


class Test_03_my_work:
    baseURL = readconfig.getApplicationURL()
    employee_id = readconfig.get_id()
    password = readconfig.get_password()
    path = ".//TestData/new_job_Testdata.xlsx"
    month = "AUG"

    def test_my_work(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.emp_id(self.employee_id)
        self.lp.password(self.password)
        self.lp.signin()
        time.sleep(3)
        self.hp = homepage(self.driver)
        self.hp.my_work_click()
        time.sleep(2)
        self.hp.my_work_datePicker_click(self.month)
        time.sleep(2)
        self.hp.job_click()
        time.sleep(2)
        actual_text = self.hp.actual_job_text()
        expected_text = self.hp.expected_job_text()
        if actual_text == expected_text:
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "mywork.png")
            assert False
        self.driver.close()