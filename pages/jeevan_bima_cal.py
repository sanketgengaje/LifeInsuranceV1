from pages.home_page import HomePage
import resources.locators as rl
from selenium.webdriver.common.alert import Alert
import time
import openpyxl

# Premium Calculator Page - class file to handle operations on page level elements
class JeevanCalculator(HomePage):
    def __init__(self, driver, test_data):
        super().__init__(driver)
        self.driver = driver
        self.test_data = test_data
        self.locator = rl.JeevancalculatorLocators(self.test_data)
        self.locator.assign_locators()

    def txt_dob(self):
        self.click(self.locator.txt_dob)
        self.date_picker_action(self.locator.date_picker_year_list, self.locator.date_picker_year, self.locator.date_picker_month_list, self.locator.date_picker_month, self.locator.date_picker_day)
    
    def txt_name_life_assured(self):
        self.enter_text(self.locator.txt_lifeAssuredFullName_locator, self.test_data[7])
        time.sleep(1)
        

    def slider_gender(self):
        if self.test_data[8] == 'F':    # If Female the slide right
            self.slider_move(self.locator.slider_gender_locator, 50)

    def slider_smoker(self):
        if self.test_data[9] == 'Y':
            self.slider_move(self.locator.slider_smoker_locator, -50)


    def sum_assured(self):
        self.drpdown_select(self.locator.drpdwn_sum_assured_list, str(self.test_data[10]))
        
    def drpdown_policy_term(self):
        self.drpdown_select(self.locator.drpdwn_policyTerm_locator, str(self.test_data[11]))

    def drpdown_premium_paying_term(self):
        if str(self.test_data[12]) == str("Single Pay"):
            option_value = "SinglePay"
        elif str(self.test_data[12]) == str(5):
            option_value = '5'
        elif str(self.test_data[12]) == str(10):
            option_value = "10"
        elif str(self.test_data[12]) == str("Regular Pay"):
            option_value = 'SameAsPolicyTerm'
        
        self.drpdown_select(self.locator.drpdwn_premium_paying_term_list, option_value)

    def drpdown_premium_frequency(self):
        if str(self.test_data[13]) == str("Annually"):
            option_value = "1"
        elif str(self.test_data[13]) == str("Half Yearly"):
            option_value = "2"
        elif str(self.test_data[13]) == str("Monthly"):
            option_value = '12'
        elif str(self.test_data[13]) == str("Single"):
            option_value = "0"

        self.drpdown_select(self.locator.drpdwn_premium_frequency_list, option_value)

    def drpdown_category(self):
        if str(self.test_data[14]) == str('None'):
            option_value = 'none'
        elif str(self.test_data[14]) == str('Staff'):
            option_value = 'staff'
        elif str(self.test_data[14]) == str('Organised Worksite Marketing'):
            option_value = 'organisedworksitemarketing'
        elif str(self.test_data[14]) == str('Corporate Worksite'):
            option_value = 'corporateworksite'
        

        self.drpdown_select(self.locator.drpdwn_staff_category, option_value)

    

    def calculate_premium(self):
        self.click(self.locator.btn_calculate_premium)   

    def capture_amount(self):
        ret_val = self.ajax_chk_text(self.locator.txt_premiumAmount_locator, self.test_data[15], 30)
        self.screenScroll_by_position(900)
        print(f"Premium Amount: {self.text_actual}")
        return ret_val

    def generate_bi(self):
        self.click(self.locator.btn_bi_locator)

    def validate_age(self):
        lbl_txt = "Maximum Maturity age for Future Generali Saral Jeevan Bima is 70 years. Kindly revise the age or PT."
        ret_val = self.ajax_chk_text(self.locator.lbl_ageValidator_locator, lbl_txt)
        self.screenScroll_by_position(700)
        print(f"Validate message: {self.text_actual}")
        return ret_val

    def validate_age_while_enter(self):
        lbl_txt = "Age should be between 18 - 65"
        ret_val = self.ajax_chk_text(self.locator.lbl_ageValidator_locator_while_enter, lbl_txt)
        self.screenScroll_by_position(200)
        time.sleep(3)
        print(f"Validate message: {self.text_actual}")
        return ret_val

    # def policy_matching_with_premium_term(self):
    #     lbl_txt = str(self.test_data[13])
    #     ret_val = self.get_disabled_txt(self.locator.drpdwn_policyTerm_locator, lbl_txt)
    #     print(f"Actual Value: {self.text_actual}")
    #     return ret_val

    def writing_in_excel(self):
        c1 = self.test_data[17]
        c1.value = "pass"
