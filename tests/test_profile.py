import time
import pytest
from pageObjects.homepageObjects import homepage
from pageObjects.loginpage import LoginPage
from utilities.readproperties import readconfig


class Test_004_login:
    baseURL = readconfig.getApplicationURL()
    employee_id = readconfig.get_id()
    password = readconfig.get_password()

    def test_profile_name(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.emp_id(self.employee_id)
        self.lp.password(self.password)
        self.lp.signin()
        time.sleep(4)
        self.hp = homepage(self.driver)
        self.hp.profile_click()
        time.sleep(3)
        actual_value = self.hp.profile_name_text()
        expected_value = "Rajesh Paswan"

        if actual_value == expected_value:
            assert True
            pass
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_profile_name.png")
            assert False, "Failure in test case: names did not match"

        self.driver.close()
