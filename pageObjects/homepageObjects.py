import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readproperties import *


class homepage:
    new_job_xpath = "//a[normalize-space()='New Job']"
    start_date_xpath = "(//div[@class='react-datepicker-wrapper']//child::input[@type='text'])[1]"
    end_date_xpath = (By.XPATH, "(//div[@class='react-datepicker-wrapper']//child::input[@type='text'])[2]")
    space_xpath = "//div[@class='row rowDataClass d-flex justify-content-center align-items-center h-100']"
    cust_details_dropdown_xpath = (By.XPATH, "//select[@name='customer']")
    select_customer_name_dropdown_xpath = "//select[@aria-label='Select Customer Name *']"
    my_works_xpath = "//div[contains(@class, 'row mt-1')]//div//p[text()='{}']"
    department_xpath = "//div//input[@name='department']"
    conveyor_no_xpath = (By.XPATH, "//div//input[@name='convRef']")
    # type_of_work_dropdown_xpath = (By.XPATH, "//div//select[@aria-label='Select Type of work *']")
    type_of_work_dropdown_xpath = "//div//select[@aria-label='Select Type of work *']"
    quantity_xpath = (By.XPATH, "//div//input[@placeholder='Quantity (nos)']")
    no_casuals_xpath = "//div//input[@name='numbercasual']"
    # submit_button_xpath = "//div//button[@type='submit']"
    submit_button_xpath = (By.XPATH, "//div//button[@type='submit']")
    success_xpath = (By.XPATH, "//h2[@id='swal2-title']")
    job_ok_btn_xpath = (By.XPATH, "//div//button[text()='OK']")
    department_conveyor_no_text = '//div[@class="card-body card-body-task"]//p[text()= "{}"]'
    type_of_work_header_in_my_work = '//div[@class="p-card rounded px-3"]//p[text()="{}"]'
    # *************************************************

    splicing_length_xpath = (By.XPATH, "//input[@placeholder='Splicing Length (mm)']")
    # type_solution_dropdown_xpath = (By.XPATH, "//select[@aria-label='Solution']")
    type_solution_dropdown_xpath = "//select[@aria-label='Solution']"
    # type_solution_dropdown_xpath = (By.XPATH, "//select[@aria-label='Solution']")
    width_xpath = (By.XPATH, "//input[@placeholder='Width (mm)']")
    solution_xpath = (By.XPATH, "//input[@placeholder='Solution (Ltr)']")
    hc_bottle_xpath = (By.XPATH, "//input[@placeholder='HC (Bottle)']")
    tic_kg_xpath = (By.XPATH, "//input[@placeholder='TIC (Kg)']")
    tcc_kg_xpath = (By.XPATH, "//input[@placeholder='TCC (Kg)']")
    type_sckit_drop_down_xpath = "//select[@aria-label='SCKit']"  # ***** ntd, 129
    face_length_xpath = (By.XPATH, "//input[@placeholder='Face Length (mm)']")
    diameter_xpath = (By.XPATH, "//input[@placeholder='Diameter (mm)']")
    sheet_length_xpath = (By.XPATH, "//input[@placeholder='Sheet Length (mm)']")
    sheet_width_xpath = (By.XPATH, "//input[@placeholder='Sheet Width (mm)']")
    sheet_thickness_xpath = (By.XPATH, "//input[@placeholder='Sheet Thickness (mm)']")
    type_sheet_xpath = "//select[@aria-label='Sheet']"  # ***** ntd ,132
    sheet_no_xpath = (By.XPATH, "// input[ @ placeholder = 'Sheet (Nos)']")
    length_xpath = (By.XPATH, "//input[@placeholder='Length (mm)']")
    thickness_xpath = (By.XPATH, "//input[@Placeholder='Thickness (mm)']")
    type_belt_path = "//select[@aria-label='Belt']"  # ****** ntd ,135
    others_xpath = (By.XPATH, "//input[@placeholder='Other']")
    number_of_casuals_xpath = (By.XPATH, "//div//input[@placeholder='Number of Casual(s) * ']")
    length_mtr_xpath = (By.XPATH, "//div//input[@placeholder='Length (Mtr)']")

    my_work_xpath = (By.LINK_TEXT, "My Works")  # ************* my work xpaths
    my_work_datePicker_xpath = "//div[@class='sort-by']/div/div/input"
    # select_month_xpath = "//div[@class='react-datepicker-wrapper']"
    my_work_job_xpath = "//p[normalize-space()='Hot Joint']"
    job_text_xpath = "//p[normalize-space()='Hot Joint']"
    expected_job_text_xpath = "//div[@class='p-card rounded px-3']/p"
    profile_xpath = (By.XPATH, "//div/a[text()='Profile']")
    profile_name_xpath = (By.XPATH, "//div[@class='card cardprofile p-4']//span[text()='Rajesh Paswan']")

    def __init__(self, driver):
        self.driver = driver

    def click_newjob(self):
        self.driver.find_element(by='xpath', value=self.new_job_xpath).click()

    def enter_start_date(self, startdate):
        self.driver.find_element(by='xpath', value=self.start_date_xpath).click()
        self.driver.find_element(by='xpath', value=self.start_date_xpath).send_keys(startdate)
        self.driver.find_element(by='xpath', value=self.start_date_xpath).send_keys(Keys.ENTER)

    def enter_end_date(self, end_date):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.end_date_xpath)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.end_date_xpath)).send_keys(
            Keys.CONTROL + 'a')
        # time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.end_date_xpath)).send_keys(
            Keys.BACKSPACE)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.end_date_xpath)).send_keys(end_date)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.end_date_xpath)).send_keys(Keys.ENTER)

    def click_on_free_space(self):
        self.driver.find_element(by='xpath', value=self.space_xpath).click()

    # **************************************************************************

    def select_option_from_dropdown_test(self, dropdown_locator, option):
        # dropdown = Select(self.driver.find_element(dropdown_locator))
        dropdown = Select(self.driver.find_element(*dropdown_locator))

        if isinstance(option, int):
            dropdown.select_by_index(option)
        elif isinstance(option, str):
            if option.isdigit():
                dropdown.select_by_index(int(option))
            elif dropdown.first_selected_option.text != option:
                dropdown.select_by_visible_text(option)
            else:
                dropdown.select_by_value(option)
        else:
            raise ValueError("Invalid option type")

    def select_option_from_dropdown(self, locator, selected_option):

        # Wait for the element to be present in the DOM
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, locator)))

        # Wait for the element to be clickable
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, locator)))

        dropdown = Select(self.driver.find_element(By.XPATH, locator))

        try:
            option_found = False
            for option in dropdown.options:
                if option.text == selected_option:
                    option.click()
                    option_found = True
                    break

            if not option_found:
                raise Exception(f"Option '{selected_option}' not found in the dropdown.")
        except Exception as e:
            print(f"Exception: {str(e)}")

        # for option in dropdown.options:
        #     if option.text == selected_option:
        #         option.click()
        #         break

    def enter_department_name(self, department_name):
        self.driver.find_element(by='xpath', value=self.department_xpath).send_keys(department_name)

    def enter_conveyor_no(self, conveyor_no):
        # self.driver.find_element(by='xpath', value=self.conveyor_no_xpath).send_keys(conveyor_no)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.conveyor_no_xpath)).send_keys(conveyor_no)

    def enter_quantity(self, quantity):
        # self.driver.find_element(by='xpath', value=self.quantity_xpath).send_keys(quantity)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.quantity_xpath)).send_keys(quantity)

    def enter_no_casuals(self, no_of_casuals):
        self.driver.find_element(by='xpath', value=self.no_casuals_xpath).send_keys(no_of_casuals)
        self.driver.find_element(by='xpath', value=self.no_casuals_xpath).send_keys(Keys.TAB)

    def click_job_submit_button(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.submit_button_xpath)).click()

    def success_is_displayed(self):
        try:
            ele = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.success_xpath))
            return ele.is_displayed()
        except Exception as e:
            print("Error:", e)
            return False

    def click_job_ok_btn(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.job_ok_btn_xpath)).click()

    def select_customer_name(self, customer_name):
        self.select_option_from_dropdown(self.select_customer_name_dropdown_xpath, customer_name)

    def validate_job_in_my_works(self, type):
        locator = self.my_works_xpath.format(type)
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, locator)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator))).click()

    def validate_job_created_in_my_works_list(self, value, type_of_work):
        locator = self.department_conveyor_no_text.format(value)
        type_of_work_header = self.type_of_work_header_in_my_work.format(type_of_work)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, type_of_work_header)))
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
            self.driver.execute_script("window.scrollTo(0,0);")
            time.sleep(3)
            return True
        except:
            # If the element is not visible, take a screenshot
            self.driver.save_screenshot(".\\Screenshots\\" + "element_not_visible.png")
            return False
            # assert False, "Element not visible. Assertion failed. Check screenshot: element_not_visible.png"

    def select_type_of_work(self, solution_type):
        self.select_option_from_dropdown(self.type_of_work_dropdown_xpath, solution_type)

    def select_type_of_solution(self, customer_name):
        self.select_option_from_dropdown(self.type_solution_dropdown_xpath, customer_name)
        # self.select_option_from_dropdown_test(self.type_solution_dropdown_xpath,customer_name)

    def select_type_sckit(self, Type_of_SCKit):
        self.select_option_from_dropdown(self.type_sckit_drop_down_xpath, Type_of_SCKit)

    def type_sheet_dp(self, type_sheet):
        self.select_option_from_dropdown(self.type_sheet_xpath, type_sheet)

    def type_belt_dp(self, type_belt):
        self.select_option_from_dropdown(self.type_belt_path, type_belt)

    def fill_splicing_length(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.splicing_length_xpath)).send_keys(
            value)

    def fill_width(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.width_xpath)).send_keys(
            value)

    def fill_solution(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.solution_xpath)).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.solution_xpath)).send_keys(value)
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.solution_xpath)).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.solution_xpath)).send_keys(value)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.solution_xpath)).send_keys(Keys.ENTER)

    def fill_hc_bottle(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.hc_bottle_xpath)).send_keys(
            value)

    def fill_tic(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.tic_kg_xpath)).send_keys(
            value)

    def fill_tcc(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.tcc_kg_xpath)).send_keys(
            value)

    def fill_face_length(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.face_length_xpath)).send_keys(
            value)

    def fill_diameter(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.diameter_xpath)).send_keys(
            value)

    def fill_sheet_length(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.sheet_length_xpath)).send_keys(
            value)

    def fill_sheet_width(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.sheet_width_xpath)).send_keys(
            value)

    def fill_sheet_thickness(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.sheet_thickness_xpath)).send_keys(
            value)

    def fill_sheet_no(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.sheet_no_xpath)).send_keys(
            value)

    def fill_length(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.length_xpath)).send_keys(
            value)

    def fill_length_mtr(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.length_mtr_xpath)).send_keys(
            value)

    def fill_thickness(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.thickness_xpath)).send_keys(
            value)

    def fill_quantity(self, value):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.quantity_xpath)).send_keys(
            value)

    def fill_others(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.others_xpath)).send_keys(
            value)

    def fill_Number_Casuals(self, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.number_of_casuals_xpath)).send_keys(
            value)

    # def select_month(self, desired_month):

    #     months = self.driver.find_elements(by='xpath', value=self.select_month_xpath)
    #     for month in months:
    #         if month.text == desired_month:
    #             month.click()

    def my_work_click(self):
        # self.driver.find_element(by='LINK_TEXT', value=self.my_work_xpath).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.my_work_xpath)).click()

    def my_work_datePicker_click(self, desired_month):
        self.driver.find_element(by='xpath', value=self.my_work_datePicker_xpath).click()
        self.driver.find_element(by='xpath', value=self.my_work_datePicker_xpath).send_keys(Keys.CONTROL + 'a')
        self.driver.find_element(by='xpath', value=self.my_work_datePicker_xpath).send_keys(Keys.BACKSPACE)
        self.driver.find_element(by='xpath', value=self.my_work_datePicker_xpath).send_keys(desired_month)

    def job_click(self):
        self.driver.find_element(by='xpath', value=self.my_work_job_xpath).click()

    def actual_job_text(self):
        ele = self.driver.find_element(by='xpath', value=self.job_text_xpath).text
        return ele

    def expected_job_text(self):
        ele = self.driver.find_element(by='xpath', value=self.expected_job_text_xpath).text
        return ele

    def profile_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.profile_xpath)).click()

    def profile_name_text(self):
        ele = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.profile_name_xpath)).text
        return ele

    def fill_details_for_my_job_creation(self, test_data, random_string):
        target_start_date = readconfig.job_date_time(2, 10, 0)
        target_end_date = readconfig.job_end_date_time(1, 3, 0)
        self.enter_start_date(target_start_date)
        self.enter_end_date(target_end_date)
        # Fill dates using date time module
        self.select_customer_name(test_data['Customer_Name'])
        time.sleep(2)
        # select department
        self.enter_department_name(test_data["Department"] + random_string)
        # select conveyor number
        self.enter_conveyor_no(test_data["Conveyor_number"])
        time.sleep(2)
        # select type of work
        self.select_type_of_work(test_data['Type_of_work'])
        time.sleep(2)
        if test_data["Splicing_length(mm)"] != " -":
            # Fill spicing length
            self.fill_splicing_length(test_data['Splicing_length(mm)'])

        if test_data["Length(mm)"] != " -":
            # Fill length
            self.fill_length(test_data["Length(mm)"])

        if test_data['Width(mm)'] != " -":
            # Fill width
            self.fill_width(test_data['Width(mm)'])

        if test_data["Thickness(mm)"] != ' -':
            # fill thickness
            self.fill_thickness(test_data["Thickness(mm)"])

        if test_data["Length (Mtr)"] != ' -':
            # fill thickness
            self.fill_length_mtr(test_data["Length (Mtr)"])

        if test_data['Select_Type_of_Belt'] != ' -':
            # fill thickness
            self.type_belt_dp(test_data['Select_Type_of_Belt'])

        if test_data["Select_Type_of_Sollution"] != " -":
            # fill others
            self.select_type_of_solution(test_data["Select_Type_of_Sollution"])

        if test_data['Solution(LTR)'] != " -":
            # Fill solution
            self.fill_solution(test_data['Solution(LTR)'])

        if test_data['TIC(Kg)'] != " -":
            # fill TIC
            self.fill_tic(test_data['TIC(Kg)'])

        if test_data['TCC(Kg)'] != " -":
            # fill TIC
            self.fill_tcc(test_data['TCC(Kg)'])

        if test_data["Face_Length(mm)"] != " -":
            # fill face length
            self.fill_face_length(test_data["Face_Length(mm)"])

        if test_data["Diameter"] != " -":
            # fill Diameter
            self.fill_diameter(test_data["Diameter"])

        if test_data["Sheet_Length(mm)"] != " -":
            # fill sheet length
            self.fill_sheet_length(test_data["Sheet_Length(mm)"])

        if test_data["Sheet_Width(mm)"] != " -":
            # fill sheet width
            self.fill_sheet_width(test_data["Sheet_Width(mm)"])

        if test_data["Sheet_Thickness(mm)"] != " -":
            # fill sheet width
            self.fill_sheet_thickness(test_data["Sheet_Thickness(mm)"])

        if test_data['Select_Type_of_SCKit'] != " -":
            # fill sheet width
            self.select_type_sckit(test_data['Select_Type_of_SCKit'])

        if test_data['HC(Bottle)'] != " -":
            # Fill hc bottle
            time.sleep(2)
            self.fill_hc_bottle(test_data['HC(Bottle)'])

        if test_data['Select_Type_of_Sheet'] != " -":
            # Fill Select_Type_of_Sheet
            self.type_sheet_dp(test_data['Select_Type_of_Sheet'])

        if test_data["Sheet(Nos)"] != " -":
            # fill sheet no's
            self.fill_sheet_no(test_data["Sheet(Nos)"])

        if test_data['Quantity(nos)'] != " -":
            # fill quantity
            self.fill_quantity(test_data['Quantity(nos)'])

        if test_data["Others"] != " -":
            # fill others
            self.fill_others(test_data["Others"])

        self.enter_no_casuals(test_data['Number_of_Casual(s)'])
        time.sleep(3)
