import allure

from data_to_use import TestData
from pages.personal_account_page import PersonalAccountPage
from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage


class TestOrderFeed:

    @allure.title('Проверка, что при клике на заказ, открывается всплывающее окно с деталями')
    def test_order_details_window_open(self, driver):
        driver.get(TestData.ORDER_FEED_PAGE)
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_on_last_order()
        assert order_feed_page.get_order_details()

    @allure.title('Проверка, что заказ пользователя из раздела История заказов отображается на странице Лента заказов')
    def test_user_order_displayed_in_history_and_feed(self, log_in_user, driver):
        driver = log_in_user
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.order_create()
        main_page.click_on_order_feed()
        order_number_main_page = order_feed_page.get_order_number_in_list()
        main_page.click_on_personal_account()
        personal_account_page.click_on_order_history()
        order_number_acc_page = personal_account_page.get_number_last_order()
        assert f'#{order_number_main_page}' == order_number_acc_page

    @allure.title('Проверка, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_all_time_order_counter_increases(self, log_in_user, driver):
        driver = log_in_user
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_on_order_feed()
        old_counter_value = order_feed_page.get_orders_for_all_time()
        main_page.click_on_constructor()
        main_page.order_create()
        main_page.click_on_order_feed()
        new_counter_value = order_feed_page.get_orders_for_all_time()
        assert new_counter_value > old_counter_value

    @allure.title('Проверка, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_today_order_counter_increases(self, log_in_user, driver):
        driver = log_in_user
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_on_order_feed()
        old_counter_value = order_feed_page.get_orders_for_today()
        main_page.click_on_constructor()
        main_page.order_create()
        main_page.click_on_order_feed()
        new_counter_value = order_feed_page.get_orders_for_today()
        assert new_counter_value > old_counter_value

    @allure.title('Проверка, что после оформления заказа его номер появляется в разделе В работе')
    def test_order_number_displayed_in_progress(self, log_in_user, driver):
        driver = log_in_user
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        order_number = main_page.order_create()
        main_page.click_on_order_feed()
        orders_in_progress = order_feed_page.get_order_number_in_progress()
        assert order_number in orders_in_progress
