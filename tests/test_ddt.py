import time
import openpyxl
import secrets
from pageObjects.homepageObjects import homepage
from pageObjects.loginpage import LoginPage
from utilities.excel_reader import ExcelReader
from utilities.readproperties import readconfig
from utilities.config import *
from utilities.excel_reader import *


class Test_job_creation_DataDrivenTest:
    excel_reader = ExcelReader("../TestData/JobCreation.xlsx", 'Sheet1')
    test_data = excel_reader.read_data()
    print(test_data[5])
    # baseURL = readconfig.getApplicationURL()
    # employee_id = readconfig.get_id()
    # password = readconfig.get_password()

    target_start_date = readconfig.job_date_time(2, 10, 0)
    target_end_date = readconfig.job_end_date_time(1, 3, 0)
    random_string = ''.join(
        secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(5))

    def test_job_creation(self, setup):
        self.driver = setup
        self.driver.get(BASE_URL)
        self.login_page = LoginPage(self.driver)
        self.login_page.login(EMPLOYEE_ID, PASSWORD)
        # Add verification of login, for example, Job Start should be displayed when login with Technician
        self.login_page.is_logged_in_for_technician()
        time.sleep(1)
        self.home_page = homepage(self.driver)
        time.sleep(1)
        self.home_page.click_newjob()
        time.sleep(1)

        for data in Test_job_creation_DataDrivenTest.test_data[4]:
            self.home_page.fill_details_for_my_job_creation(data, self.random_string)
            # click submit button
            self.home_page.click_job_submit_button()
            time.sleep(2)
            # if self.home_page.success_is_displayed() is True:
            #     assert "test passed"
            # else:
            #     self.driver.save_screenshot(".\\Screenshots\\" + "job_Creation.png")
            #     assert "test failed unsuccessful in creating  new job "
            self.home_page.click_job_ok_btn()
            time.sleep(2)
            self.home_page.my_work_click()
            time.sleep(2)
            self.home_page.validate_job_in_my_works(data["Type_of_work"])
            time.sleep(2)
            # value = str(data["Conveyor_number"]) + " - " + (data["Department"] + self.random_string).upper()
            value = "e" + str(data["Conveyor_number"])+" - "+(data["Department"]+self.random_string).upper()
            self.home_page.validate_job_created_in_my_works_list(value, data["Type_of_work"])
            self.home_page.click_newjob()
            time.sleep(3)



