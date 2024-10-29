from selenium import webdriver
import time
import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_google():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")
    assert driver.title == "Google"
    driver.quit()

def test_facebook():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://www.facebook.com/')
    assert driver.title == "facebook"
    driver.quit()

def test_instagram():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://www.instagram.com/')
    assert driver.title == "Instagram"
    driver.quit()

def test_gmail():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://www.gmail.com')
    assert driver.title == "Gmail"
    driver.quit()