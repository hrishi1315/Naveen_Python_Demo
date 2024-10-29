import time
import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/windows')  #https://rahulshettyacademy.com/AutomationPractice/
driver.maximize_window()

driver.find_element(By.LINK_TEXT, 'Click Here').click()
a = driver.window_handles  # Get the handles of all the windows that are currently open
driver.switch_to.window(a[1]) # Perform the Switch operation once the window handle ID of the desired tab is found using the switch_to. window method.
print(driver.find_element(By.XPATH, '//h3').text)