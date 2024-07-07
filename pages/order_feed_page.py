import allure

from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step('Нажатие на последний заказ')
    def click_on_last_order(self):
        return self.click_on_item(OrderFeedPageLocators.LAST_ORDER)

    @allure.step('Отображение деталей заказа')
    def get_order_details(self):
        return self.check_visibility(OrderFeedPageLocators.ORDER_DETAILS)

    @allure.step('Получение заказов в ленте заказов')
    def get_order_number_in_list(self):
        return self.item_text(OrderFeedPageLocators.ORDER_FEED_LIST)

    @allure.step('Получение моего номера заказа')
    def get_order_number_in_progress(self):
        self.waiting_for_item_to_be_visible(OrderFeedPageLocators.ORDER_IN_PROGRESS_NUMBER)
        return self.item_text(OrderFeedPageLocators.ORDER_IN_PROGRESS_NUMBER)

    @allure.step('Получение количества выполненных заказов за всё время')
    def get_orders_for_all_time(self):
        return self.item_text(OrderFeedPageLocators.ORDERS_FOR_ALL_TIME)

    @allure.step('Получение количества выполненных заказов за сегодня')
    def get_orders_for_today(self):
        return self.item_text(OrderFeedPageLocators.ORDERS_FOR_TODAY)
