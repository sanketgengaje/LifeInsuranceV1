from msilib import PID_REVNUMBER
import pytest
import pytest_html
import test_driver as td
import globals
from selenium import webdriver
from base_test import BaseTest
from pages.home_page import HomePage
from pages.premium_calculator import PremiumCalculator
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

    def bi_care_plus(self):
        test_data = self.get_test_data(self.file_name, self.test_name) # getting the test data in a list
        self.setup_test()
        try:
            premium_calculator = PremiumCalculator(self.driver, test_data)

            # Step 1
            step_desc = "Click Calculate Premium >Term insurance >Care Plus"
            step_num = 1
            home_page = HomePage(self.driver) 
            home_page.click_calculate_premium_care_plus()
            self.test_step_status_log('p', step_num, step_desc)

            # Step 2
            step_desc = "Enter data in DOB"
            step_num = 2
            premium_calculator.txt_dob()
            self.test_step_status_log('p', step_num, step_desc)

            # Step 3
            step_desc = "Enter the name assured"
            step_num = 3
            premium_calculator.txt_name_life_assured()
            self.test_step_status_log('p', step_num, step_desc)
            
            # Step 4
            step_desc = "Move the Gender slider"
            step_num = 4
            premium_calculator.slider_gender()
            self.test_step_status_log('p', step_num, step_desc)

            # Step 5
            step_desc = "Move the Smoker slider"
            step_num = 5
            premium_calculator.slider_smoker()
            self.test_step_status_log('p', step_num, step_desc)

            # Step 6
            step_desc = "Select the Option"
            step_num = 6
            premium_calculator.drpdown_option()
            self.test_step_status_log('p', step_num, step_desc)

            # Step 7
            step_desc = f"Enter sum assured: {test_data[11]}"
            step_num = 7
            premium_calculator.sum_assured()
            time.sleep(5)
            self.test_step_status_log('p', step_num, step_desc)

            # Step 8          
            step_desc = "Select Premium Payment Type"
            step_num = 8
            premium_calculator.drpdown_premium_payment_type()
            self.test_step_status_log('p', step_num, step_desc)

            # Step 9
            step_desc = "Select Policy Term"
            step_num = 9
            premium_calculator.drpdown_policy_term()
            self.test_step_status_log('p', step_num, step_desc)

            # Step 10
            step_desc = "Select Premium Frequency"
            step_num = 10
            premium_calculator.drpdown_frequency()
            self.test_step_status_log('p', step_num, step_desc)

            # Step 11
            step_desc = "Select Category"
            step_num = 11
            premium_calculator.drpdown_category()
            self.test_step_status_log('p', step_num, step_desc)

            # Step 12
            step_desc = "Select Payout Type"
            step_num = 12
            premium_calculator.drpdown_payout_type()
            self.test_step_status_log('p', step_num, step_desc)

            # Step 13
            if test_data[18] is not None:
                if len(test_data[18].strip()) > 0:
                    step_desc = "Select Payout Term"
                    step_num = 13
                    premium_calculator.drpdown_payout_term()
                    self.test_step_status_log('p', step_num, step_desc)

            # Step 14
            if test_data[19] > 0:
                step_desc = "Select Accidental Death Sum Assured"
                step_num = 14
                premium_calculator.accidental_sum_assured()
                self.test_step_status_log('p', step_num, step_desc)

            # Step 15
            step_desc = "Click on Calculate button"
            step_num = 15
            premium_calculator.calculate_premium()
            self.test_step_status_log('p', step_num, step_desc)

            if self.test_name == 'test_010':
                step_desc = "Checking Policy term & paying term value being matched"
                step_num = 16
                if premium_calculator.policy_matching_with_premium_term():
                    self.test_step_status_log('p', step_num, step_desc)
                else:
                    self.test_step_status_log('f', step_num, step_desc)  
                    pytest.fail()

            # Step 16
            if self.test_name == 'test_011':
                step_desc = "Check total number of age in policy term"
                step_num = 16
                if premium_calculator.get_total_age():
                    self.test_step_status_log('p', step_num, step_desc)
                else:
                    self.test_step_status_log('f', step_num, step_desc)  
                    pytest.fail()
            

            # Step 16
            if self.test_name == 'test_005':
                step_desc = "Check age validate message"
                step_num = 16
                if premium_calculator.validate_age():
                    self.test_step_status_log('p', step_num, step_desc)
                else:
                    self.test_step_status_log('f', step_num, step_desc)  
                    pytest.fail()

            if self.test_name == 'test_008':
                step_desc = "Check age validate message while entering"
                step_num = 16
                if premium_calculator.validate_age_while_enter():
                    self.test_step_status_log('p', step_num, step_desc)
                else:
                    self.test_step_status_log('f', step_num, step_desc)  
                    pytest.fail()

            

            if self.test_name == 'test_001' or self.test_name == 'test_002' or self.test_name == 'test_003' or \
                                            self.test_name == 'test_004' or self.test_name == 'test_006'  \
                                                or self.test_name == 'test_007' or self.test_name == 'test_009':
                # Step 16
                step_desc = "Check the premium calculated"
                step_num = 16
                if premium_calculator.capture_amount():
                    self.test_step_status_log('p', step_num, step_desc)
                else:
                    self.test_step_status_log('f', step_num, step_desc)
                    pytest.fail()

                # # Step 17
                # step_desc = "Generate BI"
                # step_num = 17
                # premium_calculator.generate_bi()
                # self.test_step_status_log('p', step_num, step_desc)
       

            time.sleep(3)

        except BaseException as e:
            err_msg = e.args[0]
            if len(err_msg) > 0:
                self.test_step_status_log('e', step_num, step_desc)
            pytest.fail(err_msg)

        finally:
            self.teardown_test()

def test_001():
    a = BenefitsIllustration(__name__, 'test_001')
    a.bi_care_plus()

def test_002():
    a = BenefitsIllustration(__name__, 'test_002')
    a.bi_care_plus()
    
def test_003():
    a = BenefitsIllustration(__name__, 'test_003')
    a.bi_care_plus()

def test_004():
    a = BenefitsIllustration(__name__, 'test_004')
    a.bi_care_plus()

def test_005():
    a = BenefitsIllustration(__name__, 'test_005')
    a.bi_care_plus()

def test_006():
    a = BenefitsIllustration(__name__, 'test_006')
    a.bi_care_plus()

def test_007():
    a = BenefitsIllustration(__name__, 'test_007')
    a.bi_care_plus()

def test_008():
    a = BenefitsIllustration(__name__, 'test_008')
    a.bi_care_plus()

def test_009():
    a = BenefitsIllustration(__name__, 'test_009')
    a.bi_care_plus()

def test_010():
    a = BenefitsIllustration(__name__, 'test_010')
    a.bi_care_plus()

def test_011():
    a = BenefitsIllustration(__name__, 'test_011')
    a.bi_care_plus()