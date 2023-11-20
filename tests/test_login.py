import time

import pytest

from pageObjects.loginpage import LoginPage
from utilities.readproperties import readconfig


class Test_001_login:
    baseURL = readconfig.getApplicationURL()
    employee_id = readconfig.get_id()
    password = readconfig.get_password()
    invalid_password = readconfig.get_invalid_password()

    login_data = [
        {"ID": employee_id, "password": password},
        {"ID": employee_id, "password": invalid_password},
    ]

    @pytest.mark.parametrize("test_input", login_data)
    def test_login(self, setup, test_input):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        id = test_input["ID"]
        password = test_input["password"]

        self.lp.emp_id(id)
        self.lp.password(password)
        self.lp.signin()
        time.sleep(5)

        if password == self.password:
            if self.lp.logo_is_displayed() is True:
                self.lp.click_logout()
                self.lp.click_button_yes()
                assert True
            else:

                assert False
        elif password == self.invalid_password:
            assert 'Incorrect username or password, please try again!' in self.lp.error_message()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_profile_name.png")
            assert False, "User is able to login with invalid credentials: Test failed"

        self.driver.close()
