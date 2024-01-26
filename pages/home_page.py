import time
from pages.base_page import BasePage
from resources.locators import HomepageLocators
from selenium.webdriver.common.action_chains import ActionChains

# Home Page - class file to handle operations on page level elements
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_calculate_premium_care_plus(self):
        self.second_level_action(HomepageLocators.menu_calculate_premium, HomepageLocators.menu_toc_term_insurance_plans, HomepageLocators.btn_calc_care_plus)
        time.sleep(1)

    def click_calculate_premium_jeevan_bima(self):
        self.second_level_action(HomepageLocators.menu_calculate_premium, HomepageLocators.menu_toc_term_insurance_plans, HomepageLocators.btn_cal_jeevan_bima)
        time.sleep(1) 
