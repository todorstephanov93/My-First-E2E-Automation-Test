import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='class')
def setup(request):
    service_object = Service("C:\\Users\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=service_object)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    return driver
