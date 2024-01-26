from selenium.webdriver.common.by import By

""" Locator file to define page wise locators """

class HomepageLocators():
    menu_calculate_premium = (By.XPATH, "//a[contains(text(), 'Calculate')]")
    menu_toc_term_insurance_plans = (By.XPATH, "/html/body/div[2]/div/div/nav/div[2]/ul/li[3]/ul/li/div/div/ul/li[1]/a")
    btn_calc_care_plus = (By.XPATH, "/html/body/div[2]/div/div/nav/div[2]/ul/li[3]/ul/li/div/div/ul/li[1]/ul/li/div/div/ul/li[1]/a")
    btn_cal_jeevan_bima = (By.XPATH, "//a[@href='/tools-and-calculators/saral-jeevan-bima-premium-calculator'][normalize-space()='Calculate']")
    
class PremiumcalculatorLocators():
    def __init__(self, test_data):
        self.test_data = test_data

    def assign_locators(self):
        self.txt_dob = (By.ID, "DateOfBirth")
        dob_parts = str(self.test_data[5]).split("-")
        day = str(int(dob_parts[0])) # To get numbers upto 9 as single digits
        month = str(int(dob_parts[1]) - 1)
        year = dob_parts[2]
        self.date_picker_year_list = (By.XPATH, "//select[@class='ui-datepicker-year']")    
        self.date_picker_year = (By.XPATH, f"//select[@class='ui-datepicker-year']//option[@value={year}]")
        self.date_picker_day = (By.XPATH, f"//td[@data-year={year}]//a[text() = {day}]")
        self.date_picker_month_list = (By.XPATH, "//select[@class='ui-datepicker-month']") 
        self.date_picker_month = (By.XPATH, f"//select[@class='ui-datepicker-month']//option[@value={month}]")

        self.txt_lifeAssuredFullName_locator = (By.ID, "txtLifeAssuredFullName")
        self.slider_gender_locator = (By.XPATH, "//div[@id='slider_gender']//span[@class='ui-slider-handle ui-state-default ui-corner-all']")
        self.slider_smoker_locator = (By.XPATH, "//div[@id='slider_smoke']//span[@class='ui-slider-handle ui-state-default ui-corner-all']")        
        self.drpdwn_option_locator = (By.XPATH, "//select[@id='ddlPlanOptions']")
        self.txt_sumAssured_locator = (By.ID, "txtSumAssuredlabeled")
        self.drpdwn_premiumPaymentType_locator = (By.XPATH, "//select[@id='ddlPremiumPaymentType']")  
        self.drpdwn_policyTerm_locator = (By.XPATH, "//select[@id='ddlPolicyTerm']")
        self.drpdwn_frequency_locator = (By.XPATH, "//select[@id='ddlFrequency']")
        self.drpdwn_category_locator = (By.XPATH, "//select[@id='ddlCategory']")
        self.drpdwn_payoutType_locator = (By.XPATH, "//select[@id='ddlPayOutType']")
        self.drpdwn_payoutTerm_locator = (By.XPATH, "//select[@id='ddlPayOutTerm']") 
        self.txt_lumpsumPercentage_locator = (By.ID, "txtLumpsumPercentage")   
        self.txt_adsa_locator = (By.ID, "txtADSAlabeled")            
        self.btn_calculate_locator = (By.ID, "Calculate")
        self.lbl_premiumAmount_locator = (By.ID, "amount")
        self.btn_bi_locator = (By.ID, "sisreport")
        self.lbl_ageValidator_locator = (By.ID, "ErrortxtAge")
        self.lbl_ageValidator_locator_while_enter = (By.XPATH, "/html/body/div[1]/div[5]/div/div[1]/div/form/div[4]/span")
        self.disble_paying_term = (By.XPATH, "/html/body/div[1]/div[5]/div/div[1]/div/form/div[10]/div[7]/div/div/div")
        self.txt_disable_age = (By.ID, "txtAge")
        self.policyterm_locator_for_max_age = (By.ID, "ddlPolicyTerm")

class JeevancalculatorLocators():
    def __init__(self, test_data):
        self.test_data = test_data

    def assign_locators(self):
        self.txt_dob = (By.ID, "DateOfBirth")
        dob_parts = str(self.test_data[5]).split("-")
        day = str(int(dob_parts[0])) # To get numbers upto 9 as single digits
        month = str(int(dob_parts[1]) - 1)
        year = dob_parts[2]
        self.date_picker_year_list = (By.XPATH, "//select[@class='ui-datepicker-year']")    
        self.date_picker_year = (By.XPATH, f"//select[@class='ui-datepicker-year']//option[@value={year}]")
        self.date_picker_day = (By.XPATH, f"//td[@data-year={year}]//a[text() = {day}]")
        self.date_picker_month_list = (By.XPATH, "//select[@class='ui-datepicker-month']") 
        self.date_picker_month = (By.XPATH, f"//select[@class='ui-datepicker-month']//option[@value={month}]")

        self.txt_lifeAssuredFullName_locator = (By.ID, "txtLifeAssuredFullName")
        self.slider_gender_locator = (By.XPATH, "//div[@id='slider_gender']//span[@class='ui-slider-handle ui-state-default ui-corner-all']")
        self.slider_smoker_locator = (By.XPATH, "//div[@id='slider_smoke']//span[@class='ui-slider-handle ui-state-default ui-corner-all']")        
        self.drpdwn_option_locator = (By.XPATH, "//select[@id='ddlPlanOptions']")
        self.txt_sumAssured_locator = (By.ID, "ddlSumAssured")
        self.drpdwn_premiumPaymentType_locator = (By.XPATH, "//select[@id='ddlPremiumPaymentType']")  
        self.drpdwn_policyTerm_locator = (By.XPATH, "//select[@id='ddlPolicyTerm']")
        self.drpdwn_frequency_locator = (By.XPATH, "//select[@id='ddlFrequency']")
        self.drpdwn_category_locator = (By.XPATH, "//select[@id='ddlCategory']")
        self.drpdwn_payoutType_locator = (By.XPATH, "//select[@id='ddlPayOutType']")
        self.drpdwn_payoutTerm_locator = (By.XPATH, "//select[@id='ddlPayOutTerm']") 
        self.txt_lumpsumPercentage_locator = (By.ID, "txtLumpsumPercentage")   
        self.txt_adsa_locator = (By.ID, "txtADSAlabeled")            
        self.btn_calculate_locator = (By.ID, "Calculate")
        self.lbl_premiumAmount_locator = (By.ID, "amount")
        self.btn_bi_locator = (By.ID, "sisreport")
        self.lbl_ageValidator_locator = (By.ID, "valGlobalErorr")
        

        # added after premium
        self.drpdwn_sum_assured_list = (By.ID, "ddlSumAssured")
        self.drpdwn_policy_term_list = (By.ID, "ddlPolicyTerm")
        self.drpdwn_premium_paying_term_list = (By.ID, "ddlPremiumPayingTerm")
        self.drpdwn_premium_frequency_list = (By.ID, "ddlFrequency")
        self.drpdwn_staff_category = (By.ID, "ddlCategory")
        
        self.btn_calculate_premium = (By.XPATH, "//div[@class='disOverlayWrap']//input[1]")
        self.txt_premiumAmount_locator = (By.ID, "amount")
        self.btn_generater_locator = (By.ID, "sisreport")
        self.lbl_ageValidator_locator_while_enter = (By.ID, "ErrortxtAge")
        self.lbl_ageValidator_locator = (By.ID, "valGlobalErorr")
        

