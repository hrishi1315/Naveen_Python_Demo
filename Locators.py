import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys('Raje')  #CSS - tagname[attribute='value']
driver.find_element(By.NAME, 'email').send_keys('frycry12@gmail.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('abc123')
driver.find_element(By.ID, 'exampleCheck1').click()

#Dropdown--
dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown.select_by_index(1)

driver.find_element(By.XPATH, "//input[@type='submit']").click()  #Xpath - //tagname[@attribute='value']
a= driver.find_element(By.CLASS_NAME, 'alert-dismissible').text
print(a)
assert 'Success' in a


time.sleep(10)
