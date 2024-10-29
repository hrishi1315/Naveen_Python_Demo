from selenium import webdriver
import time
import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = None

def setup_module(module):
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(6)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")

def teardown_mdoule(module):
    driver.quit()

#1st TC
def test_google_tittle():
    assert driver.title == "Google"
#2nd TC
def test_google_url():
    assert driver.current_url == "https://www.google.com/"
