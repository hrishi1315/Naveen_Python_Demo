from selenium import webdriver
import time
import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = None

@pytest.fixture(scope='module')    # (@) annotation==decorator
def initialize_driver():      #precondition will work-- mhnje ha purna code TC chya adhi run hoil.
    global driver
    print("===============================Setup=========================")
    driver = webdriver.Chrome()
    driver.implicitly_wait(6)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")

    yield                     #postcondition -- mhnje ha code sagle TC tun zalyvr execute hoil last la..
    print("===============================Teardown=======================")
    driver.quit()

#1st TC
@pytest.mark.usefixtures("initialize_driver")   #@pytest.mark.usefixtures-- helps you manage and apply fixtures more easily in your tests, keeping your code organized and clear
def test_google_tittle():
    assert driver.title == "Google"
#2nd TC
@pytest.mark.usefixtures("initialize_driver")
def test_google_url(initialize_driver):
    assert driver.current_url == "https://www.google.com/"
