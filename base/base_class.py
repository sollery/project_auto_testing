import datetime

from selenium.webdriver import Keys


class Base:
    def __init__(self, driver):
        self.driver = driver


    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'current url {get_url}')

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")


    """Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot{}.png'.format(now_date)
        self.driver.save_screenshot('C:\\project_auto_testing\\screen\\' + name_screenshot)
        print('screenshot taken')

    """Method assert word"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        print(get_url)
        assert get_url == result,f'{get_url}'
        print("Good value url")

    """Method press enter"""
    def press_enter(self,name_input):
        name_input.send_keys(Keys.RETURN)
        print('click enter')





