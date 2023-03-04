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

    # Getters

    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart)))

    def get_cart_link(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_link)))

    # Actions

    def click_button_add_to_cart(self):
        self.get_button_add_to_cart().click()
        print('click button add to cart')

    def click_cart_link(self):
        action = ActionChains(self.driver)
        action.double_click(self.get_cart_link()).perform()
        print('click cart')

    # Methods

    def product_add_to_cart(self):
        self.get_current_url()
        self.click_button_add_to_cart()
        self.click_cart_link()
        time.sleep(10)
        self.assert_url('https://www.regard.ru/cart')

        # self.get_screenshot()