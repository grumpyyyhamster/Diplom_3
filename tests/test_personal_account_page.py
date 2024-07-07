import allure

from data_to_use import TestData
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:

    @allure.title('Проверка перехода по клику на Личный кабинет')
    def test_personal_account_redirect(self, log_in_user, driver):
        driver = log_in_user
        personal_account_page = PersonalAccountPage(driver)
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        expected_link = personal_account_page.get_url_personal_account_page()
        assert expected_link == TestData.PERSONAL_ACC_PAGE

    @allure.title('Проверка перехода в раздел История заказов')
    def test_history_order_redirect(self, log_in_user, driver):
        driver = log_in_user
        personal_account_page = PersonalAccountPage(driver)
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        personal_account_page.click_on_order_history()
        expected_link = personal_account_page.get_url_personal_account_page()
        assert expected_link == TestData.ORDERS_HISTORY

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, log_in_user, driver):
        driver = log_in_user
        personal_account_page = PersonalAccountPage(driver)
        main_page = MainPage(driver)
        main_page.click_on_personal_account()
        personal_account_page.click_logout()
        expected_link = personal_account_page.get_url_personal_account_page()
        assert expected_link == TestData.LOGIN_PAGE
