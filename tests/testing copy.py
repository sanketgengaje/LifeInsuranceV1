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
driver.find_element(By.XPATH, "//a[@href='/tools-and-calculators/care-plus-premium-calculator'][normalize-space()='Calculate']")
time.sleep(3)
# alert = Alert(driver)
# alert.dismiss()
a = 2002
driver.find_element(By.ID, "DateOfBirth").click()
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//select[@class='ui-datepicker-year']"))).click()      
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, f"//select[@class='ui-datepicker-year']//option[@value={a}]"))).click()      
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//select[@class='ui-datepicker-month']"))).click()      
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, f"//select[@class='ui-datepicker-month']//option[@value={8}]"))).click()      
WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, f"//td[@data-year={2002}]//a[text() = {7}]"))).click()

policy_term = Select(driver.find_element(By.ID, "ddlPolicyTerm"))
policy_term.select_by_value("29")
#Select class for dropdown
l= Select(driver.find_element(By.ID, "ddlPremiumPayingTerm"))
l.select_by_value("SinglePay")
d= (l)
print('Options are: ')
#iterate over dropdown options
for opt in d.options:
#get option text
   print(opt.text)
# premium_freq = Select(driver.find_element(By.ID, "ddlFrequency"))
# premium_freq.select_by_value("2")
Select_CATEGORY = Select(driver.find_element(By.ID, "ddlCategory"))
Select_CATEGORY.select_by_value("corporateworksite")

print("done")



# ------compare policy logic----------
# Element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[5]/div/div[1]/div/form/div[10]/div[7]/div/div/div")))
# # driver.execute_script("arguments[0].removeAttribute('disabled')", Element)
# print(Element.text)
time.sleep(10)
driver.quit()