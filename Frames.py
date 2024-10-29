import time
import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/iframe')  #https://rahulshettyacademy.com/AutomationPractice/
driver.maximize_window()
driver.implicitly_wait(5)

driver.switch_to.frame('mce_0_ifr')  # In frame
driver.find_element(By.ID, 'tinymce').send_keys(" Agli baar Modi Sarkar..!!!!")
driver.switch_to.default_content()  # Out from the frame & back in Webdriver

