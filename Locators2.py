import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/client')  #https://rahulshettyacademy.com/AutomationPractice/
driver.maximize_window()

driver.find_element(By.LINK_TEXT, 'Forgot password?').click()
driver.find_element(By.XPATH, '//form/div[1]/input').send_keys('abc@gmail.com')
driver.find_element(By.XPATH, "//div/input[@id='userPassword']").send_keys('123654')
driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys('123654')
driver.find_element(By.XPATH, "//button[@type='submit']").click()  # By using 'text()'=//button[text()='Save New Password']










time.sleep(6)