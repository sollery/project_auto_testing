import time

from base.base_class import Base
from secret_data import login, password
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CatalogPage(Base):
    url = 'https://www.regard.ru/catalog/1537/kompyutery-i-noutbuki'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    laptops_link = '//*[@id="__next"]/div/div/main/div/div[3]/div[2]/div/div[1]/div/a'
    price_min = '//*[@id="__next"]/div/div/main/div/div[2]/div/div/div/div/div/div/div[1]/section/div[2]/div/div/div/div/input[1]'
    price_max = '//*[@id="__next"]/div/div/main/div/div[2]/div/div/div/div/div/div/div[1]/section/div[2]/div/div/div/div/input[2]'
    checkbox_manufacturer = '//label[@for="id-ASUS-ASUS"]'
    checkbox_cpu = '//label[@for="id-Core-i7-2094"]'
    button_peculiarities = '//*[@id="__next"]/div/div/main/div/div[2]/div/div/div/div/div/div/div[3]/section'
    checkbox_peculiarities = '//label[@for="id-подсветка-клавиатуры-5274"]'
    button_filter_color = '//*[@id="__next"]/div/div/main/div/div[2]/div/div/div/div/div/div/section[25]/div[1]'
    checkbox_color = '//label[@for="id-серебристый-2529"]'
    product_link = '//*[@id="__next"]/div/div/main/div/div[3]/div[3]/div/div/div[1]/div[1]/div/div[1]/div[2]/a'

    # Getters

    def get_laptops_link(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.laptops_link)))

    def get_price_min(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_min)))

    def get_price_max(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_max)))

    def get_checkbox_manufacturer(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_manufacturer)))

    def get_checkbox_cpu(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_cpu)))

    def get_button_peculiarities(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_peculiarities)))

    def get_checkbox_peculiarities(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_peculiarities)))

    def get_button_filter_color(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_filter_color)))

    def get_checkbox_color(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkbox_color)))

    def get_product_link(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_link)))





    # Actions

    def click_laptops_link(self):
        self.get_laptops_link().click()
        print('click laptops link')

    def input_price_min(self,value):
        self.get_price_min().send_keys(value)
        print('input price min')

    def input_price_max(self,value):
        self.get_price_max().send_keys(value)
        print('input price max')

    def click_checkbox_manufacturer(self):
        self.get_checkbox_manufacturer().click()
        print('click manufacturer')

    def click_checkbox_cpu(self):
        self.get_checkbox_cpu().click()
        print('click cpu')

    def click_button_peculiarities(self):
        self.get_button_peculiarities().click()
        print('click button peculiarities')

    def click_checkbox_peculiarities(self):
        self.get_checkbox_peculiarities().click()
        print('click checkbox peculiarities')

    def click_button_filter_color(self):
        self.get_button_filter_color().click()
        print('click button filter color')

    def click_checkbox_color(self):
        self.get_checkbox_color().click()
        print('click check box color')

    def click_product_link(self):
        # action = ActionChains(self.driver)
        # action.double_click(self.get_product_link())
        # self.driver.execute_script("return arguments[0].scrollIntoView(true);",self.get_product_link())
        # time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.get_product_link())
        print('click product link')




    # Methods

    def select_product_filters(self):
        self.get_current_url()
        self.click_laptops_link()
        self.input_price_min('50000')
        self.input_price_max('100000')
        self.click_checkbox_manufacturer()
        self.click_checkbox_cpu()
        self.click_button_peculiarities()
        self.click_checkbox_peculiarities()
        self.click_button_filter_color()
        self.click_checkbox_color()
        self.click_product_link()
        time.sleep(10)
        self.assert_url('https://www.regard.ru/product/447296/noutbuk-asus-x515ja-vivobook-15-bq2527')

        # self.get_screenshot()