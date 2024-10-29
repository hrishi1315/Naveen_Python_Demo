import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions

file_path = "C:/Users/Admin/Downloads/download"

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://rahulshettyacademy.com/upload-download-test/index.html')
driver.maximize_window()
driver.find_element(By.ID, "downloadButton").click()
a = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
a.send_keys(file_path)


wait = WebDriverWait=(driver,5)
Toastify = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
wait.until(expected_conditions.visibility_of_element_located(Toastify))
print(driver.find_element(*Toastify).text)