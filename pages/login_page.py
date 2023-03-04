import time

from base.base_class import Base
from secret_data import login, password
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(Base):

    url = 'https://www.regard.ru/login/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    private_office = '//*[@id="__next"]/div/div/div/div/div/div/div[1]/div/div[2]/div[1]/div'
    login = '//input[@name="login"]'
    password = '//input[@name="password"]'
    login_button = '//*[@id="__next"]/div/div/main/div/div/form/button'

    # Getters

    def get_login(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_private_office(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.private_office)))


    # Actions

    def input_login(self, email):
        self.get_login().send_keys(email)
        print('input user name')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('input password')

    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')

    def click_private_office(self):
        self.get_private_office().click()
        print('Click private office')

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.get_current_url()
        self.click_private_office()
        self.input_login(login)
        self.input_password(password)
        self.click_login_button()
        time.sleep(3)
        self.assert_url('https://www.regard.ru/profile')
        # self.get_screenshot()
