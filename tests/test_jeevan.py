from msilib import PID_REVNUMBER
import pytest
import pytest_html
import test_driver as td
import globals
from selenium import webdriver
from base_test import BaseTest
from pages.home_page import HomePage
from pages.jeevan_bima_cal import JeevanCalculator
import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.alert import Alert

class BenefitsIllustration(BaseTest):
    def __init__(self, file_name, test_name):
        super().__init__()
        self.file_name = file_name
        self.test_name = test_name

    def setup_test(self):
        self.setup_class()

    def teardown_test(self):
        self.teardown_class()

    def bi_jeevan_bima(self):
        test_data = self.get_test_data(self.file_name, self.test_name) # getting the test data in a list
        self.setup_test()
        try:
            jeevan_bima_calculator = JeevanCalculator(self.driver, test_data)

            # Step 1
            step_desc = "Click Calculate Premium >Term insurance >Jeevan Bima"
            step_num = 1
            home_page = HomePage(self.driver) 
            home_page.click_calculate_premium_jeevan_bima()
            self.test_step_status_log('p', step_num, step_desc)

            # Step 2
            step_desc = "Enter data in DOB"
            step_num = 2
            jeevan_bima_calculator.txt_dob()
            self.test_step_status_log('p', step_num, step_desc)

            # Exceptional Step for age above 65 calculation test_003
            if self.test_name == 'test_003':
                step_desc = "Check age validate message while entering"
                step_num = 3
                if jeevan_bima_calculator.validate_age_while_enter():
                    self.test_step_status_log('p', step_num, step_desc)
                    return                  
                else:
                    self.test_step_status_log('f', step_num, step_desc)  
                    pytest.fail()
            # Exceptional Step for age below 18 calculation test_002
            if self.test_name == 'test_002':
                step_desc = "Check age validate message while entering"
                step_num = 3
                if jeevan_bima_calculator.validate_age_while_enter():
                    self.test_step_status_log('p', step_num, step_desc)
                    return                  
                else:
                    self.test_step_status_log('f', step_num, step_desc)  
                    pytest.fail()
            

            # Step 3
            step_desc = "Enter the name assured"
            step_num = 3
            jeevan_bima_calculator.txt_name_life_assured()
            self.test_step_status_log('p', step_num, step_desc)

            # Step 4
            step_desc = "Move the Gender slider"
            step_num = 4
            jeevan_bima_calculator.slider_gender()
            self.test_step_status_log('p', step_num, step_desc)

            # Step 5
            step_desc = "Move the Smoker slider"
            step_num = 5
            jeevan_bima_calculator.slider_smoker()
            self.test_step_status_log('p', step_num, step_desc)

            # Step 6
            step_desc = f"Enter sum assured: {test_data[10]}"
            step_num = 6
            jeevan_bima_calculator
            jeevan_bima_calculator.sum_assured()
            self.test_step_status_log('p', step_num, step_desc)
            
            # Step 7
            step_desc = "Select policy term"
            step_num = 7
            jeevan_bima_calculator.drpdown_policy_term()
            self.test_step_status_log('p', step_num, step_desc)
                
            # Step 8
            step_desc = "Select premium paying term"
            step_num = 8
            jeevan_bima_calculator.drpdown_premium_paying_term()
            self.test_step_status_log('p', step_num, step_desc)
                
            # Step 9
            step_desc = "Select premium frequency"
            step_num = 9
            jeevan_bima_calculator.drpdown_premium_frequency()
            self.test_step_status_log('p', step_num, step_desc)

            # Step 10
            step_desc = "Select Category"
            step_num = 10
            jeevan_bima_calculator.drpdown_category()
            self.test_step_status_log('p', step_num, step_desc)

            # Step 11
            step_desc = "Click on Calculate button"
            step_num = 11
            jeevan_bima_calculator.calculate_premium()
            self.test_step_status_log('p', step_num, step_desc)

            # Exceptional Step for age below 18 calculation test_004
            if self.test_name == 'test_004':
                step_desc = "Check maximum maturity age"
                step_num = 3
                if jeevan_bima_calculator.validate_age():
                    self.test_step_status_log('p', step_num, step_desc)
                    pytest.fail()                   
                else:
                    self.test_step_status_log('f', step_num, step_desc)  
                    pytest.fail()

            # Step 12
            step_desc = "Compare both values"
            step_num = 12
            jeevan_bima_calculator.capture_amount()
            self.test_step_status_log('p', step_num, step_desc)

            # step_desc = "writing in excel"
            # step_num = 17
            # jeevan_bima_calculator.capture_amount()
            # self.test_step_status_log('p', step_num, step_desc)
            # jeevan_bima_calculator.writing_in_excel()
            
            # # Step 13
            # step_desc = "Generate BI"
            # step_num = 17
            # jeevan_bima_calculator.generate_bi()
            # self.test_step_status_log('p', step_num, step_desc)

            time.sleep(2)
            

            

        except BaseException as e:
            err_msg = e.args[0]
            if len(err_msg) > 0:
                self.test_step_status_log('e', step_num, step_desc)
            pytest.fail(err_msg)

        finally:
            self.teardown_test()

def test_001():
    a = BenefitsIllustration(__name__, 'test_001')
    a.bi_jeevan_bima()

def test_002():
    a = BenefitsIllustration(__name__, 'test_002')
    a.bi_jeevan_bima()

def test_003():
    a = BenefitsIllustration(__name__, 'test_003')
    a.bi_jeevan_bima()

def test_004():
    a = BenefitsIllustration(__name__, 'test_004')
    a.bi_jeevan_bima()

def test_005():
    a = BenefitsIllustration(__name__, 'test_005')
    a.bi_jeevan_bima()

def test_006():
    a = BenefitsIllustration(__name__, 'test_006')
    a.bi_jeevan_bima()

def test_007():
    a = BenefitsIllustration(__name__, 'test_007')
    a.bi_jeevan_bima()