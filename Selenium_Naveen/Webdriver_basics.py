from selenium import webdriver
import time
import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import webdriver_manager.chrome import ChromeDriverManager


Browsername = 'chrome'

if Browsername == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())