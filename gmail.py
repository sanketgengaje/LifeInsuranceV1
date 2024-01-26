from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Open the browser and go to the Gmail website
driver = webdriver.Chrome()
driver.execute_script("window.open('https://mail.google.com/')")

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

# Enter the email and password and click on the sign-in button
email_input = driver.find_element(By.XPATH, "//input[@type='email']")
# email_input = driver.find_element_by_xpath("//input[@type='email']")
email_input.send_keys("sanketgengaje1@gmail.com")
time.sleep(3)
email_input.send_keys(Keys.RETURN)
time.sleep(5)

password_input = driver.find_element(By.XPATH,"//input[@type='password']")
password_input.send_keys("Gs@nket2306")
password_input.send_keys(Keys.RETURN)

time.sleep(20) # wait for 5 seconds
driver.quit() # close the browser window
