import time
import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://www.globalsqa.com/samplepagetest/')

driver.find_element(By.CLASS, 'wpcf7-form-control wpcf7-file').click()

a = Select(driver.find_element(By.ID, 'g2599-experienceinyears')

a.select_by_index(1)

driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()

alert = driver.switch_to.alert

print(alert.text)

alert.accept()