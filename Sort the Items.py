from selenium import webdriver
from selenium.webdriver.common.by import By

Veg = []
driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')
driver.maximize_window()

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggieList = driver.find_elements(By.XPATH, "//tr/td[1]")

for i in veggieList:
    Veg.append(i.text)
    OriginalVeg = Veg
    Veg.sort()

assert Veg == OriginalVeg