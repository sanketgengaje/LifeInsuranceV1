from pages.home_page import HomePage
import resources.locators as rl
from selenium.webdriver.common.alert import Alert
import time
# Premium Calculator Page - class file to handle operations on page level elements
class PremiumCalculator(HomePage):
    def __init__(self, driver, test_data):
        super().__init__(driver)
        self.driver = driver
        self.test_data = test_data
        self.locator = rl.PremiumcalculatorLocators(self.test_data)
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

    def drpdown_option(self):
        if self.test_data[10] == 'Life Cover':
            option_value = 'T36'
        elif self.test_data[10] == 'Extra Life Cover':
            option_value = 'T37'

        self.drpdown_select(self.locator.drpdwn_option_locator, option_value)

    def sum_assured(self):
        self.enter_text(self.locator.txt_sumAssured_locator, self.test_data[11])

    def drpdown_premium_payment_type(self):
        self.drpdown_select(self.locator.drpdwn_premiumPaymentType_locator, self.test_data[12])

    def drpdown_policy_term(self):
        self.drpdown_select(self.locator.drpdwn_policyTerm_locator, str(self.test_data[13]))

    def drpdown_frequency(self):
        if self.test_data[15] == 'Annually':
            option_value = '1'
        elif self.test_data[15] == 'Half Yearly':
            option_value = '2'
        elif self.test_data[15] == 'Quarterly':
            option_value = '6'
        elif self.test_data[15] == 'Monthly':
            option_value = '12'

        self.drpdown_select(self.locator.drpdwn_frequency_locator, option_value)

    def drpdown_category(self):
        if self.test_data[16] == 'Staff':
            option_value = 'staff'
        elif self.test_data[16] == 'General':
            option_value = 'General'

        self.drpdown_select(self.locator.drpdwn_category_locator, option_value)

    def drpdown_payout_type(self):
        if self.test_data[17] == 'Lumpsum':
            option_value = 'Lumpsum'
        elif self.test_data[17] == 'Fixed Income':
            option_value = 'Fixed'
        elif self.test_data[17] == 'Mixed':
            option_value = 'Mixed'

        self.drpdown_select(self.locator.drpdwn_payoutType_locator, option_value)

    def drpdown_payout_term(self):
        if self.test_data[18] == '60 Months':
            option_value = '60'
        elif self.test_data[18] == '120 Months':
            option_value = '120'

        self.drpdown_select(self.locator.drpdwn_payoutTerm_locator, option_value)

    def lumpsum_percentage(self):
        self.enter_text(self.locator.txt_lumpsumPercentage_locator, self.test_data[20])

    def accidental_sum_assured(self):
        self.enter_text(self.locator.txt_adsa_locator, self.test_data[19]) 

    def calculate_premium(self):
        self.click(self.locator.btn_calculate_locator)   

    def capture_amount(self):
        ret_val = self.ajax_chk_text(self.locator.lbl_premiumAmount_locator, self.test_data[21], 30)
        self.screenScroll_by_position(1000)
        print(f"Premium Amount: {self.text_actual}")
        return ret_val

    def generate_bi(self):
        self.click(self.locator.btn_bi_locator)

    def validate_age(self):
        lbl_txt = "Age should be between 18 - 65"
        ret_val = self.ajax_chk_text(self.locator.lbl_ageValidator_locator, lbl_txt)
        self.screenScroll_by_position(800)
        print(f"Validate message: {self.text_actual}")
        return ret_val

    def validate_age_while_enter(self):
        lbl_txt = "Age should be between 18 - 65"
        ret_val = self.ajax_chk_text(self.locator.lbl_ageValidator_locator_while_enter, lbl_txt)
        self.screenScroll_by_position(200)
        print(f"Validate message: {self.text_actual}")
        return ret_val

    def policy_matching_with_premium_term(self):
        lbl_txt = str(self.test_data[13])
        ret_val = self.get_disabled_txt(self.locator.disble_paying_term, lbl_txt)
        print(f"Policy term: {self.test_data[13]}, Premium paying term: {self.text_actual}")
        return ret_val

    def get_total_age(self):
        ret_val = self.addition1(self.locator.txt_disable_age, self.locator.policyterm_locator_for_max_age)
        print(f"User age: {self.age}, User can get max number of policy of: {self.max_policy_no}")
        return ret_val