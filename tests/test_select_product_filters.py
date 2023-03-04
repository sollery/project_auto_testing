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

def test_select_product_filters():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service('C:\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=g, options=options)
    login = LoginPage(driver)
    login.authorization()
    main_page = MainPage(driver)
    main_page.select_category()
    catalog_page = CatalogPage(driver)
    catalog_page.select_product_filters()
    time.sleep(10)