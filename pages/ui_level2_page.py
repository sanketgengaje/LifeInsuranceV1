from pages.home_page import HomePage
import resources.locators as rl
from selenium.webdriver.common.alert import Alert
# from resources.locators import HomepageLocators, DynamicIdLocators

class Level2Page(HomePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.alert_text_check = ""        

    def click_dynamic_id_btn(self):
        self.click(rl.DynamicIdLocators.btn_dynamic_id)

    def click_class_attribute_btn(self):
        self.click(rl.ClassAttributeLocators.btn_class_attributes)
    
    def class_attribute_check_alert_text(self):
        self.alert_text_expected = "Primary button pressed and"
        if self.chk_alert_text(self.alert_text_expected):
            return True
        else:
            return False

    def click_alert_accept(self):
        self.handle_alert("accept")
    
    def click_hidden_layers_btn(self):
        e = self.click(rl.HiddenLayersLocator.btn_hidden_layers)
        return e
    
    def click_load_delay_btn(self):
        self.click(rl.LoadDelayLocators.btn_load_delay)

    def click_ajax_btn(self):
        self.click(rl.AjaxLocators.btn_ajax)

    def ajax_btn_check_text(self):
        self.text_expected = "Data loaded with AJAX get request."
        return self.ajax_chk_text(rl.AjaxLocators.ajax_label_text, self.text_expected)

    def click_ajax_client_delay_btn(self):
        self.click(rl.AjaxLocators.btn_ajax)

    def ajax_client_delay_check_text(self):
        self.text_expected = "Data calculated on the client side."
        return self.ajax_chk_text(rl.AjaxLocators.ajax_label_text, self.text_expected)

    def click_mouse_click_btn(self):
        self.mouse_click(rl.MouseClickLocators.btn_mouse_click)

    def send_text_input(self):
        text = "Kunal Sabnis"
        self.enter_text(rl.TextInputLocators.text_input, text)
        self.click(rl.TextInputLocators.btn_text_input)

    def click_scrollbars_hiding_btn(self):
        self.click_scroll_btn(rl.ScrollbarsLocator.btn_scrollbars_hiding)

    def check_dynamic_table_values(self):
        # To be completed
        hdr_col_index = self.get_tbl_col_hdr_pos(rl.DynamicTableLocators.ele_tbl_hdr_locator, "CPU")
        print('Hdr col pos', str(hdr_col_index))
        tbl_cell_val = self.get_tbl_row_val(rl.DynamicTableLocators.ele_table_cell_locator, "Chrome", hdr_col_index)
        print(tbl_cell_val)
        chrome_label_text_words = self.get_label_text(rl.DynamicTableLocators.chrome_check_locator).split()

        print(chrome_label_text_words[2])
        if tbl_cell_val.strip() == chrome_label_text_words[2].strip():
            return True
        else:
            return False

        

