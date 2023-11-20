import configparser
from datetime import datetime, timedelta

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class readconfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'URL')
        return url

    @staticmethod
    def get_id():
        emp_id = config.get('common info', 'ID')
        return emp_id


    @staticmethod
    def get_password():
        password = config.get('common info', 'PASSWORD')
        return password

    @staticmethod
    def get_invalid_password():
        invalid_password = config.get('common info', 'INVALID_PASSWORD')
        return  invalid_password

    @staticmethod
    def job_date_time(days_before, hour, minute):
        # this will Calculate the date `days_before` days before the current date
        today = datetime.today()
        target_date = today - timedelta(days=days_before)
        target_datetime = datetime(target_date.year, target_date.month, target_date.day, hour, minute)
        formatted_date = target_datetime.strftime("%d-%m-%Y %I:%M %p")
        return formatted_date

    @staticmethod
    def job_end_date_time(days_before, hour, minute):
        # Calculate the date `days_before` days before the current date
        today = datetime.today()
        target_date = today - timedelta(days=days_before)
        target_datetime = datetime(target_date.year, target_date.month, target_date.day, hour, minute)
        formatted_date = target_datetime.strftime("%d-%m-%Y %I:%M %p")
        return formatted_date

    @staticmethod
    def get_customer_name():
        customer_name = config.get('common info', 'customer_name')
        return customer_name

    @staticmethod
    def get_department():
        department = config.get('common info', 'department')
        return department

    @staticmethod
    def get_Conveyor_Number():
        Conveyor_Number = config.get('common info', 'Conveyor Number')
        return Conveyor_Number

    @staticmethod
    def get_Work_Details():
        Work_Details = config.get('common info', 'Work Details')
        return Work_Details

    @staticmethod
    def get_Material_Details_quantity():
        Material_Details = config.get('common info', 'Material Details quantity')
        return Material_Details

    @staticmethod
    def get_number_of_casual():
        number_of_casual = config.get('common info', 'number of casual')
        return number_of_casual


