import time
import driver
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')  #https://rahulshettyacademy.com/AutomationPractice/
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('ber')
time.sleep(2)

search = driver.find_elements(By.XPATH, "//div[@class='products']/div")
a = (len(search))
assert a == 3