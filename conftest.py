import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireFoxOptions

from data_to_use import TestData
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(params=['Chrome', 'Fox'], scope='function')
def driver(request):
    if request.param == 'Chrome':
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif request.param == 'Fox':
        options = FireFoxOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def log_in_user(driver):
    driver.get(TestData.MAIN_PAGE)
    main_page = MainPage(driver)
    main_page.click_on_login()
    login_page = LoginPage(driver)
    login_page.email_input(TestData.EMAIL)
    login_page.input_password(TestData.PASSWORD)
    login_page.click_log_in()
    return driver
