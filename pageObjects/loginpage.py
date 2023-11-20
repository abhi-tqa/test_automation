from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    Employee_id_xpath = "//div//input[@placeholder='Employee ID']"
    Password_xpath = "//div//input[@type='password']"
    signin_click = "//div//button[text()='Sign In']"
    splice_logo = (By.XPATH, "//img[@class='icon-header']")
    error_message_xpath = "//p[normalize-space()='Incorrect username or password, please try again!']"
    logout_xpath = "//div[text()='Logout']"
    yes_button_xpath = "//div//button[text()='Yes']"
    job_start_option = "//b[text()='Job Start']"

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = self.driver.find_element(By.XPATH, self.Employee_id_xpath)
        password_field = self.driver.find_element(By.XPATH, self.Password_xpath)
        login_button = self.driver.find_element(By.XPATH, self.signin_click)

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

    def is_logged_in_for_technician(self):
        # Wait until the element is displayed
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.job_start_option))
        )

    def emp_id(self, id):
        self.driver.find_element(by='xpath', value=self.Employee_id_xpath).send_keys(id)

    def password(self, password):
        self.driver.find_element(by='xpath', value=self.Password_xpath).send_keys(password)

    def signin(self):
        self.driver.find_element(by='xpath', value=self.signin_click).click()

    def logo_is_displayed(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.splice_logo)
            )
            return element.is_displayed()
        except:
            return False

    def click_logout(self):
        self.driver.find_element(by='xpath', value=self.logout_xpath).click()

    def click_button_yes(self):
        self.driver.find_element(by='xpath', value=self.yes_button_xpath).click()

    def error_message(self):
        error_message = self.driver.find_element(by='xpath', value=self.error_message_xpath).text
        print(error_message)
        return error_message
    # assert "Invalid password" in error_message.text
