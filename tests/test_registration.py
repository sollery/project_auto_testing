import time

from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.registration_form import RegistrationForm
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options


def test_registration(driver):
    reg_form = RegistrationForm(driver)
    reg_form.registration()
    time.sleep(10)


def test_show_password(driver):
    reg_form = RegistrationForm(driver)
    reg_form.show_password()


