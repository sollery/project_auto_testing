import time

from base.base_class import Base
from secret_data import login, password
from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationForm(Base):
    url = 'https://www.regard.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    link_private_office = '//*[@id="__next"]/div/div/div/div/div/div/div[1]/div/div[2]/div[1]/div/span'
    button_registration = '//*[@id="AUTHORIZATION_MODAL_WRAPPER"]/button[2]'
    email_form = '//*[@id="AUTHORIZATION_MODAL_WRAPPER"]/form/div[1]/div/input[2]'
    name_form = '//*[@id="AUTHORIZATION_MODAL_WRAPPER"]/form/div[2]/div/input[2]'
    phone_form = '//*[@id="AUTHORIZATION_MODAL_WRAPPER"]/form/div[3]/div/input[2]'
    password_form = '//*[@id="AUTHORIZATION_MODAL_WRAPPER"]/form/div[4]/div[1]/input[2]'
    password_confirmation_form = '//*[@id="AUTHORIZATION_MODAL_WRAPPER"]/form/div[5]/div/input[2]'
    submit_registration = '//*[@id="AUTHORIZATION_MODAL_WRAPPER"]/form/button'

    # Getters

    def get_link_private_office(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.link_private_office)))

    def get_button_registration(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_registration)))

    def get_email_form(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email_form)))

    def get_name_form(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.name_form)))
    
    def get_phone_form(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phone_form)))
    
    def get_password_form(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password_form)))
    
    def get_password_confirmation_form(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password_confirmation_form)))
    
    def get_submit_registration(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.submit_registration)))
    
    

    # Actions

    def click_link_private_office(self):
        self.get_link_private_office().click()
        print('Click link private_office')

    def click_button_registration(self):
        self.get_button_registration().click()
        print('Click button registration')

    def input_email_form(self,email):
        self.get_email_form().send_keys(email)
        print('input email form')

    def input_name_form(self, name):
        self.get_name_form().send_keys(name)
        print('input name form')

    def input_phone_form(self, phone):
        self.get_phone_form().send_keys(phone)
        print('input phone form')

    def input_password_form(self, password):
        self.get_password_form().send_keys(password)
        print('input password form')

    def input_password_confirmation_form(self, password):
        self.get_password_confirmation_form().send_keys(password)
        print('input password confirmation form')

    def click_submit_registration(self):
        self.get_submit_registration().click()
        print('Click submit registration')

    # Methods

    def registration(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_link_private_office()
        self.click_button_registration()
        self.input_email_form('test@mail.ru')
        self.input_name_form('test')
        self.input_phone_form('9999999999')
        self.input_password_form('111111aA')
        self.input_password_confirmation_form('111111aA')
        self.click_submit_registration()

        # self.get_screenshot()
