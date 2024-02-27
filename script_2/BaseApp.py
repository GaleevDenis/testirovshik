from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://sbis.ru/contacts"
        self.partners = False
        self.partners_2 = False
        self.kod_region = False

    def find_element(self, locator, time = 10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time = 10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator))
        
    def check_click(self, locator, time = 10):
        return WebDriverWait(self.driver,time).until(EC.visibility_of_element_located(locator))