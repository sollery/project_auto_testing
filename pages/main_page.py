import time

from base.base_class import Base
from secret_data import login, password
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(Base):

    url = 'https://www.regard.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    button_catalog = '//*[@id="__next"]/div/div/div/div/div/div/div[1]/div/button'
    category_link = '//*[@id="__next"]/div/div/div/div/div/div/div[2]/div/div/div/div/div/ul/a[4]/div'

    # Getters

    def get_button_catalog(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_catalog)))

    def get_category_link(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.category_link)))



    # Actions
    def click_button_catalog(self):
        self.get_button_catalog().click()
        print('click button catalog')

    def click_category_link(self):
        self.get_category_link().click()
        print('click category catalog')

    # Methods

    def select_category(self):
        self.driver.get(self.url)
        self.driver.delete_all_cookies()
        self.get_current_url()
        self.click_button_catalog()
        self.click_category_link()
        time.sleep(3)
        self.assert_url('https://www.regard.ru/catalog/1537/kompyutery-i-noutbuki')
        # self.get_screenshot()