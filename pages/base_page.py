from argparse import Action
from asyncio.windows_events import NULL
from unittest.mock import Base
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class BasePage():

    def __init__(self, driver):
        """ This function is called for every new instance of BasePage class """

        self.driver = driver
    def drpdown_select(self, by_locator, option_value, wait_time=10):
        select_ele = Select(WebDriverWait(self.driver, wait_time).until(ec.presence_of_element_located(by_locator), "Timeout occured while locating dropdwon element"))
        select_ele.select_by_value(option_value)

    def drpdown_select_visible_txt(self, by_locator, option_value, wait_time=10):
        select_ele = Select(WebDriverWait(self.driver, wait_time).until(ec.presence_of_element_located(by_locator), "Timeout occured while locating dropdwon element"))
        select_ele.select_by_visible_text(option_value)
        

    def slider_move(self, by_locator, offset, wait_time=10):
        slider_bar = WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(by_locator), "Timeout occured while locating slider element")
        actions = ActionChains(self.driver)
        actions.click_and_hold(slider_bar).move_by_offset(offset, 0).release().perform()
        # actions.drag_and_drop_by_offset(slider_bar, offset, 0)
        # actions.perform()

    def second_level_action(self, by_locator_hover1, by_locator_hover2, by_locator_click, wait_time=10):
        hover_ele1 = WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(by_locator_hover1), "Timeout occured in locating first hover element")
        actions = ActionChains(self.driver)
        actions.move_to_element(hover_ele1)
        actions.perform()

        hover_ele2 = WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(by_locator_hover2), "Timeout occured in locating second hover element")        
        actions.move_to_element(hover_ele2)
        actions.perform()

        WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(by_locator_click), "Timeout occured in locating click element").click()

    def date_picker_action(self, by_locator_year_list, by_locator_year, by_locator_month_list, by_locator_month, by_locator_day, wait_time=10):
        WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(by_locator_year_list), "Timeout occured in locating date picker year list").click()      
        WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(by_locator_year), "Timeout occured in locating year").click()      
        WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(by_locator_month_list), "Timeout occured in locating date picker month list").click()      
        WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(by_locator_month), "Timeout occured in locating month").click()      
        WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(by_locator_day), "Timeout occured in locating day").click()      

    def mouse_click(self, by_locator, wait_time=10):
        ele = WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(by_locator), "Timeout occured in locating physical mouse click button" )
        actions = ActionChains(self.driver)
        actions.move_to_element(ele)
        actions.click(ele)
        actions.perform()
   
    def click(self, by_locator, wait_time=10):
        """ For click actions """
        WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(by_locator), "Timeout occured on click").click()
    
    def click_scroll_btn(self, by_locator, wait_time=10):
        """ For bringing the element into view by scrolling"""
        self.err_msg = ""
        try:
            ele = WebDriverWait(self.driver, wait_time).until(ec.presence_of_element_located(by_locator), "Timeout occured while finding the hidden button")
            actions = ActionChains(self.driver)
            actions.move_to_element(ele)
            actions.click(ele)
            actions.perform()
        except BaseException as e:
            self.err_msg = e.args[0]

    def enter_text(self, by_locator, text, wait_time=10):
        """ To enter text in text box """
        WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(by_locator), "Timeout occurred while text entry").send_keys(text)

    def get_title(self, title, wait_time=10):
        """ To get the window title """
        self.err_msg = ""
        try:
            WebDriverWait(self.driver, wait_time).until(ec.title_is(title), "Timeout occurred while getting the window title")
            return self.driver.title
        except BaseException as e:
            self.err_msg = e.args[0]

    def handle_alert(self, action):

        self.err_msg = ""
        try:
            alert = Alert(self.driver)            
            if action == "accept":
                alert.accept()
            elif action == "dismiss":
                alert.dismiss()
            elif action == "text":
                print(alert.text)
            else:
                pass
        except BaseException as e:
            self.err_msg = e.args[0]

    def chk_alert_text(self, alert_text_expected):

        self.err_msg = ""
        self.alert_text_actual = ""
        try:
            alert = Alert(self.driver)
            self.alert_text_actual = alert.text
            if self.alert_text_actual == alert_text_expected:
                return True
            else:
                return False
        except BaseException as e:
            self.err_msg = e.args[0]
            return False

    def ajax_chk_text(self, by_locator, text_expected, wait_time=10):

        self.err_msg = ""
        self.text_actual = ""
        ele = WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(by_locator), "Timeout occurred while locating the element")
        self.text_actual = ele.text
        if ele.text == text_expected:
            return True
        else:
            return False
    def get_tbl_col_hdr_pos(self, by_locator, col_hdr_text, wait_time=10):
        hdr_ele_list = WebDriverWait(self.driver, wait_time).until(ec.visibility_of_all_elements_located(by_locator), "Timeout occurred while locating the element")        
        return [ele.text for ele in hdr_ele_list].index(col_hdr_text)

    def get_tbl_row_val(self, by_locator, row_cell_text, hdr_index, wait_time=10):
        row_ele_list = WebDriverWait(self.driver, wait_time).until(ec.visibility_of_all_elements_located(by_locator), "Timeout occurred while locating the element")
        row_index = [ele.text for ele in row_ele_list].index(row_cell_text)
        return row_ele_list[hdr_index + row_index].text

    def get_label_text(self, by_locator, wait_time=10):
        label_text = WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(by_locator), "Timeout occurred while locating the element").text
        return label_text

    def chk_visibilty_from_slct_option(self, by_locator, wait_time=10):
        ele = self.driver.find_element(by_locator)
        if ele.is_displayed():
            return True
        else:
            return False

    def get_disabled_txt(self, by_locator, text_expected, wait_time=10):

        self.text_actual = ""
        ele = WebDriverWait(self.driver, wait_time).until(ec.presence_of_element_located(by_locator), "Timeout occurred while locating the element")
        # self.driver.execute_script("arguments[0].removeAttribute('disabled')", ele)
        self.text_actual = ele.text
        if ele.text == text_expected:
            return True
            
        else:
            return False

    def addition(self, by_locator, wait_time=10):
        
        age_txt = self.driver.find_element(By.ID, "txtAge")
        first = age_txt.text

        self.text_actual = ""
        element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, "ddlPolicyTerm")))
        actual_text = element.text
        second = actual_text[-2]+ actual_text[-1]
        total_age = int(first) + int(second)
        
        if total_age == int(85):
            return True
        else:
            return True

    def addition1(self, age_loctor, by_locator2, wait_time=10):
        select_ele = WebDriverWait(self.driver, wait_time).until(ec.presence_of_element_located(age_loctor), "Timeout occurred while locating the element")
        self.age = select_ele.text

        element1 = Select(WebDriverWait(self.driver, wait_time).until(ec.presence_of_element_located(by_locator2), "Timeout occured while locating dropdwon element"))
        self.max_policy_no =""
        for option in element1.options:
            a = option.text
            #print(option.text)
        self.max_policy_no = a
        if int(self.max_policy_no)+ int(self.age) == 85:
            return True
        else:
            return False

    def screenScroll_by_locator(self, by_locator, wait_time=10):
        scroll = WebDriverWait(self.driver, wait_time).until(ec.visibility_of_element_located(by_locator), "Timeout occurred while locating the element")
        self.driver.execute_script("arguments[0].scrollIntoView()",scroll)

    def screenScroll_by_position(self, position):
        self.driver.execute_script(f"window.scrollTo(0, {position})")
            
            



