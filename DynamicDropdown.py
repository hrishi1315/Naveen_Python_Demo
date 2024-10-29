import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')  #https://rahulshettyacademy.com/AutomationPractice/
driver.maximize_window()
driver.find_element(By.ID, 'autosuggest').send_keys('ind')
time.sleep(3)
country = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

print(len(country))

for i in country:
    if i.text == 'India':
        i.click()

#print(driver.find_element(By.ID, 'autosuggest').get_attribute('value'))
assert (driver.find_element(By.ID, 'autosuggest').get_attribute('value')) == 'India'