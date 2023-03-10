import time

import pytest
from pages.profile_page import ProfilePage
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options


def test_authorization(driver):
    login = LoginPage(driver)
    login.authorization()


def test_logout(driver):
    login = LoginPage(driver)
    login.authorization()
    profile_page = ProfilePage(driver)
    profile_page.logout_s()




