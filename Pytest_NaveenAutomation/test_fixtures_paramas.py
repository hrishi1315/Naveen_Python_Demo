from selenium import webdriver
import driver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(params=['chrome'],scope='class')
def initialize_driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        request.cls.driver = driver
    yield driver
    driver.close()

@pytest.mark.usefixtures("initialize_driver")
class BaseChrome:
    pass
class Test_Google(BaseChrome):

    def test_google(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"

   