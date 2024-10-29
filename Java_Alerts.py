import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')  #https://rahulshettyacademy.com/AutomationPractice/
driver.maximize_window()

o = 'Akash'

driver.find_element(By.CSS_SELECTOR, '#name').send_keys(o)
driver.find_element(By.CSS_SELECTOR, '#confirmbtn').click()

alert = driver.switch_to.alert
print(alert.text)  # it will print alert msg
time.sleep(10)
assert o in alert.text

alert.accept()  # it will click on 'ok' button on alert
#alert.dismiss() # it will click on 'cancel' button on alert



