from selenium import webdriver
import time
import driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope='class')
def initialize_chromedriver(request):
    ch_driver = webdriver.Chrome()
    request.cls.driver = ch_driver
    yield
    ch_driver.close()

@pytest.fixture(scope='class')
def initialize_ff(request):
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = ff_driver
    yield
    ff_driver.close()

@pytest.mark.usefixtures("initialize_chromedriver")
class Base_Chrome_Test:       # Parent class
    pass
class Test_Chrome_Test(Base_Chrome_Test):  #Child class mdhe Parent class
    def test_google_title_chrome(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"

@pytest.mark.usefixtures("initialize_ff")
class Base_Firefox_Test:       # Parent class
    pass
class Test_Firefox_Test(Base_Firefox_Test):  #Child class mdhe Parent class
    def test_google_title_firefox(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"