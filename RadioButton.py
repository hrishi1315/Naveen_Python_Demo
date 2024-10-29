from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')  #https://rahulshettyacademy.com/AutomationPractice/
driver.maximize_window()

r = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
r[2].click()
assert r[2].is_selected()

driver.find_element(By.NAME, "show-hide").is_displayed()  # is_displayed() -- will check is it displayed or not