import time

from base.base_class import Base
from secret_data import login, password
from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(Base):
    url = 'https://www.regard.ru/cart'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    button_clear_cart = '//*[@id="__next"]/div/div/main/div/div[1]/div/div[2]/div/span[3]/button'
    button_accept_clear = '//*[@id="CONFIRMATION_MODAL_WRAPPER"]/div[2]/button'
    button_catalog = '//*[@id="__next"]/div/div/main/div/div[2]/div/a'
    city = '//input[@id="userTown"]'
    checkbox_way_to_get = '//*[@id="__next"]/div/div/main/div/div[2]/form/div[2]/div[1]/label[1]'
    address = '//input[@id="recepientAddress"]'
    porch = '//input[@id="porchNum"]'
    floor = '//input[@id="floor"]'
    flat = '//input[@id="officeOrFlat"]'
    date_picker = '//*[@id="__next"]/div/div/main/div/div[2]/form/div[2]/div[3]/div/div[1]/div/div/div/div'
    button_date = '//div[@aria-label="Thu Mar 16 2023"]'
    time = '//*[@id="__next"]/div/div/main/div/div[2]/form/div[2]/div[3]/div/div[2]'
    select_time = '//*[@id="__next"]/div/div/main/div/div[2]/form/div[2]/div[3]/div/div[2]/div/ul/li[2]/span'
    checkbox_payment_method = '//*[@id="__next"]/div/div/main/div/div[2]/form/div[3]/div/label[3]/div[1]/span'
    user_name = '//input[@id="userName"]'
    email = '//input[@id="userEmail"]'
    telephone = '//input[@id="userPhone"]'
    checkbox_accept_manager = '//*[@id="__next"]/div/div/main/div/div[2]/form/div[4]/div/div[5]/label/span[2]/label'
    information = '//textarea[@id="additionalInfo"]'





    # Getters

    def get_button_clear_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_clear_cart)))

    def get_button_accept_clear(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_accept_clear)))

    def get_button_catalog(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_catalog)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_checkbox_way_to_get(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_way_to_get)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_porch(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.porch)))

    def get_floor(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.floor)))

    def get_flat(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.flat)))

    def get_date_picker(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.date_picker)))

    def get_button_date(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_date)))

    def get_time(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.time)))

    def get_select_time(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_time)))

    def get_checkbox_payment_method(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_payment_method)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_telephone(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.telephone)))

    def get_checkbox_accept_manager(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_accept_manager)))

    def get_information(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.information)))



    # Actions

    def click_button_clear_cart(self):
        self.driver.execute_script("arguments[0].click();", self.get_button_clear_cart())
        print('click button clear cart')

    def click_button_accept_clear(self):
        self.get_button_accept_clear().click()
        print('cart clear')

    def click_button_catalog(self):
        self.get_button_catalog().click()
        print('cart clear, click button catalog')

    def input_city(self,city):
        self.get_city().clear()
        self.get_city().send_keys(city)
        print('input city')

    def click_checkbox_way_to_get(self):
        self.get_checkbox_way_to_get().click()
        print('checkbox_way_to_get click')

    def input_address(self,address):
        self.get_address().clear()
        self.get_address().send_keys(address)
        print('input address')

    def input_porch(self,porch):
        self.get_porch().clear()
        self.get_porch().send_keys(porch)
        print('input porch')

    def input_floor(self,floor):
        self.get_floor().clear()
        self.get_floor().send_keys(floor)
        print('input floor')

    def input_flat(self,flat):
        self.get_flat().clear()
        self.get_flat().send_keys(flat)
        print('input flat')

    def click_date_picker(self):
        self.get_date_picker().click()
        print('click_date_picker')

    def click_button_date(self):
        self.get_button_date().click()
        print('click button date')

    def click_time(self):
        self.get_time().click()
        print('click time')

    def click_select_time(self):
        self.get_select_time().click()
        print('click select time')

    def click_checkbox_payment_method(self):
        self.get_checkbox_payment_method().click()
        print('click payment method')

    def input_user_name(self,name):
        self.get_user_name().clear()
        self.get_user_name().send_keys(name)
        print('input name')

    def input_email(self,email):
        self.get_email().clear()
        self.get_email().send_keys(email)
        print('input email')

    def input_telephone(self,telephone):
        self.get_telephone().clear()
        self.get_telephone().send_keys(telephone)
        print('input telephone')

    def click_checkbox_accept_manager(self):
        self.get_checkbox_accept_manager().click()
        print('click accept manager')

    def input_information(self,info):
        self.get_information().clear()
        self.get_information().send_keys(info)


    # Methods

    def clear_cart(self):
        self.get_current_url()
        self.get_current_url()
        self.click_button_clear_cart()
        self.click_button_accept_clear()

    def filling_inputs(self):
        self.get_current_url()
        self.input_city('test')
        self.click_checkbox_way_to_get()
        self.input_address('testovaya')
        self.input_porch('22')
        self.input_floor('5')
        self.input_flat('110')
        self.click_date_picker()
        self.click_button_date()
        self.click_time()
        self.click_select_time()
        # print(self.get_button_date().get_attribute('value'))
        self.click_checkbox_payment_method()
        self.input_user_name('test')
        self.input_email('test@mail.ru')
        self.input_telephone('9889999999')
        self.click_checkbox_accept_manager()
        self.input_information('testtest')
        time.sleep(10)





