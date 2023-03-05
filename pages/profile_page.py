import time

from base.base_class import Base
from secret_data import login, password
from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage(Base):
    # url = 'https://www.regard.ru/profile/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    link_private_office = '//*[@id="__next"]/div/div/div/div/div/div/div[1]/div/div[2]/div[1]/a/div'
    button_logout = '//*[@id="__next"]/div/div/main/div/div[2]/div/div/div/div[1]/div/div/div/div/a[1]'
    button_personal_data = '//*[@id="__next"]/div/div/main/div/div[2]/div/div/div/div[1]/div/div/div/div/a[2]'

    # Getters

    def get_button_logout(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_logout)))

    def get_button_personal_data(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_personal_data)))

    def get_link_private_office(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.link_private_office)))

    # Actions

    def click_button_logout(self):
        # self.get_button_logout().click() #elementnotinteractableexception
        self.driver.get('https://www.regard.ru/profile/logout') #elementnotinteractableexception

        print('Click button logout')

    def click_link_private_office(self):
        self.get_link_private_office().click()

        print('Click link private_office')

    def click_button_personal_data(self):
        self.get_button_personal_data().click()

        print('Click button personal_data')

    # Methods

    def logout_s(self):
        self.get_current_url()
        self.click_button_logout()


        # self.get_screenshot()
