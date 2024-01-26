import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" :2}
# chrome_options.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome()
driver.get("https://life.futuregenerali.in/")
driver.maximize_window()

actions = ActionChains(driver)
hover1 = driver.find_element(By.XPATH, "//a[contains(text(), 'Calculate')]")
actions.move_to_element(hover1)
actions.perform()

hover2 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/nav/div[2]/ul/li[3]/ul/li/div/div/ul/li[1]/a")
actions.move_to_element(hover2)
actions.perform()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@href='/tools-and-calculators/care-plus-premium-calculator'][normalize-space()='Calculate']").click()
time.sleep(3)
# alert = Alert(driver)
# alert.dismiss()
driver.find_element(By.ID, "DateOfBirth").click()
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//select[@class='ui-datepicker-year']"))).click()      
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, f"//select[@class='ui-datepicker-year']//option[@value={2002}]"))).click()      
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//select[@class='ui-datepicker-month']"))).click()      
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, f"//select[@class='ui-datepicker-month']//option[@value={8}]"))).click()      
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, f"//td[@data-year={2002}]//a[text() = {7}]"))).click()

#----get disable age text----
age_txt = driver.find_element(By.ID, "txtAge")
first = age_txt.text

#----- Age Slider movement ---------
time.sleep(5)
slider_bar = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//div[@id='slider_gender']//span[@class='ui-slider-handle ui-state-default ui-corner-all']")))
actions.click_and_hold(slider_bar).move_by_offset(50, 0).release().perform()
# actions.drag_and_drop_by_offset(slider_bar, 100, 0)
# actions.perform()
time.sleep(5)

# finding max value----------
actual_text = ""
element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "ddlPolicyTerm")))
actual_text = element.text
second = actual_text[-2]+ actual_text[-1]
final_age = int(first) + int(second)
if final_age == 85:
    print(final_age)
    print("pass")
else:
    print("fail")


# finding max value---------
actual_text = ""
option = 0
# element1 = Select(WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "ddlPolicyTerm"))))
element1 = Select(driver.find_element(By.ID, "ddlPolicyTerm"))
b =""
for option in element1.options:
    a = option.text
    #print(option.text)
b = a
age_txt = driver.find_element(By.ID, "txtAge")
first = age_txt.text 
if int(b) + int(first) ==85:
    print("correct")  
else:
    print("incorrect")
print("end")
get_value = Select(driver.find_element(By.ID, "ddlPolicyTerm"))
get_value.select_by_index(1)
o= get_value.first_selected_option
print(o.text)
get_value2 = Select(driver.find_element(By.ID, "ddlPolicyTerm"))
for option1 in get_value2.options:
    c = (option1.text)
    print(c)
##


# #Select class for dropdown
# l= Select(driver.find_element(By.ID, "ddlPolicyTerm"))
# d= (l)
# print('Options are: ')
# #iterate over dropdown options
# for opt in d.options:
# #get option text
#    print(opt.text)
# print (max(d))
# #browser quit
# driver.quit()



# ------compare policy logic----------
# Element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[5]/div/div[1]/div/form/div[10]/div[7]/div/div/div")))
# # driver.execute_script("arguments[0].removeAttribute('disabled')", Element)
# print(Element.text)
time.sleep(10)
driver.quit()