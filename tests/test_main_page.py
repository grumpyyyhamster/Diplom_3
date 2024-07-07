import allure

from data_to_use import TestData
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestMainFunctions:

    @allure.title('Переход по клику на Конструктор')
    def test_constructor_redirect(self, driver):
        driver.get(TestData.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_on_constructor()
        expected_link = main_page.get_url_main_page()
        assert expected_link == TestData.MAIN_PAGE

    @allure.title('Переход по клику на Лента заказов')
    def test_order_feed_redirect(self, driver):
        driver.get(TestData.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_on_order_feed()
        expected_link = main_page.get_url_main_page()
        assert expected_link == TestData.ORDER_FEED_PAGE

    @allure.title('Проверка появления всплывающего окна с деталями при нажатии на ингридиент')
    def test_ingredient_details_window(self, driver):
        driver.get(TestData.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_on_ingredient_bun()
        assert 'Детали ингредиента' in main_page.check_ingredient_details_label()

    @allure.title('Проверка закрытия всплывающего окна с деталями ингредиента')
    def test_ingredient_details_window_close(self, driver):
        driver.get(TestData.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.click_on_ingredient_bun()
        main_page.close_ingredient_details()
        main_page.check_invisibility_ingredient_details()
        assert main_page.check_visibility(MainPageLocators.INGREDIENTS_DETAILS_LABEL).is_displayed() == False

    @allure.title('Проверка, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_counter_ingredient_increase(self, driver):
        driver.get(TestData.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient_in_order()
        assert main_page.get_ingredient_count() == '2'

    @allure.title('Проверка оформления заказа залогиненным пользователем')
    def test_auth_user_can_place_order(self, log_in_user, driver):
        driver = log_in_user
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient_in_order()
        main_page.click_on_order_button()
        assert main_page.check_visibility(MainPageLocators.ORDER_STATUS_TEXT).is_displayed() == True
