from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/seleniumPractise/')
driver.maximize_window()

a = driver.find_element(By.XPATH, '//td[5]/p')
sum = 0

for i in a:
    sum = sum + int(a.text)
print(sum)

totalamt = int(driver.find_element(By.CSS_SELECTOR, '.totAmt'))
assert sum == totalamt