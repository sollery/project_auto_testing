import time

from base.base_class import Base
from secret_data import login, password
from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(Base):
    url = 'https://www.regard.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    button_add_to_cart = '//*[@id="__next"]/div/div/main/div/div[1]/div[3]/div/div[2]/div[2]/div[1]/button'
    cart_link = '//*[@id="__next"]/div/div/div/div/div/div/div[1]/div/div[2]/div[4]/div'
    title_product = '//*[@id="__next"]/div/div/main/div/div[1]/div[1]/span/h1'
    price_product = '//*[@id="__next"]/div/div/main/div/div[1]/div[3]/div/div[2]/div[1]/div/div/span'
    cart_product = '//*[@id="__next"]/div/div/main/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div/a'
    cart_price = '//*[@id="__next"]/div/div/main/div/div[3]/div/div/div/form/div[1]/p[1]/span'

    # Getters

    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart)))

    def get_cart_link(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_link)))

    def get_title_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.title_product))).text

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_product))).text

    def get_cart_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_product))).text

    def get_cart_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_price))).text


    # Actions

    def click_button_add_to_cart(self):
        self.get_button_add_to_cart().click()
        print('click button add to cart')

    def click_cart_link(self):
        action = ActionChains(self.driver)
        action.double_click(self.get_cart_link()).perform()
        print('click cart')

    def assert_title_product(self, product_page_title, cart_page_title):
        print(product_page_title)
        print('*'*8)
        print(cart_page_title)
        assert product_page_title == cart_page_title,'FAILED PRODUCT PRICE'
        print('PASS PRODUCTS TITLE')


    def assert_price_product(self, product_page_price, cart_page_price):
        assert product_page_price == cart_page_price,'FAILED PRODUCT PRICE'
        print('PASS PRODUCTS PRICE')

    # Methods

    def product_add_to_cart(self):
        self.get_current_url()
        product = self.get_title_product()
        product_price = self.get_price_product()
        self.click_button_add_to_cart()
        self.click_cart_link()
        cart = self.get_cart_product()
        cart_price = self.get_cart_price()
        self.assert_title_product(product, cart)
        self.assert_price_product(product_price, cart_price)
        self.assert_url('https://www.regard.ru/cart')



        # self.get_screenshot()