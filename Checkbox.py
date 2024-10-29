import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')  #https://rahulshettyacademy.com/AutomationPractice/
driver.maximize_window()

s = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(s))

for i in s:
    if i.get_attribute("value") == "option2":
        i.click()
        assert i.is_selected()
        break