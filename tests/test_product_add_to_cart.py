from pages.cart_page import CartPage
from pages.product_page import ProductPage
import time
import pytest
from pages.catalog_page import CatalogPage
from pages.main_page import MainPage
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options


def test_product_add_to_cart(driver):
    login = LoginPage(driver)
    login.authorization()
    cart_page = CartPage(driver)
    # cart_page.clear_cart()
    main_page = MainPage(driver)
    main_page.select_category()
    catalog_page = CatalogPage(driver)
    catalog_page.select_product_filters()
    product_page = ProductPage(driver)
    product_page.product_add_to_cart()
    cart_page.filling_inputs()
    cart_page.clear_cart()
    time.sleep(10)
