import time
import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/AutomationPractice/')  #https://rahulshettyacademy.com/AutomationPractice/
driver.maximize_window()

action = ActionChains (driver)

action.move_to_element(driver.find_element(By.ID, 'mousehover')).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, 'Reload')).click().perform()

# Double click
action.double_click(driver.find_element(By.ID, 'mousehover')).perform()

# Right click
action.context_click(driver.find_element(By.ID, 'mousehover')).perform()

