import time

from base.base_class import Base
from secret_data import login, password
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(Base):
    url = 'https://www.regard.ru/profile/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    button_logout = '//*[@id="__next"]/div/div/main/div/div[2]/div/div/div/div[1]/div/div/div/div/a[1]/svg'

    # Getters

    def get_button_logout(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_logout)))



    # Actions

    def click_button_logout(self):
        self.get_button_logout().click()
        print('Click button logout')

    # Methods

    def logout(self):
        self.get_current_url()
        self.driver.refresh()
        self.click_button_logout()

        # self.get_screenshot()