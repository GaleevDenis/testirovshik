import pytest
from selenium import webdriver
from selenium import webdriver
import pytest
import time
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window
    options = webdriver.ChromeOptions()
    options.add_argument("--proxy-server=138.128.91.65:8800")
    driver.implicitly_wait(2)
    options.add_argument('--headless')
    options.add_argument("start-maximized")
    yield driver
    driver.close()
    driver.quit()