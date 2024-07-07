import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Нажатие на кнопку Конструктор')
    def click_on_constructor(self):
        self.click_on_item(MainPageLocators.CONSTRUCTOR_HEADER)

    @allure.step('Нажать на кнопку Лента заказов')
    def click_on_order_feed(self):
        self.click_on_item(MainPageLocators.ORDER_FEED_HEADER)

    @allure.step('Нажатие на кнопку Личный кабинет')
    def click_on_personal_account(self):
        self.click_on_item(MainPageLocators.PERSONAL_ACCOUNT_HEADER)

    @allure.step('Нажатие на кнопку Войти в аккаунт')
    def click_on_login(self):
        self.click_on_item(MainPageLocators.LOGIN_BUTTON)

    @allure.step('Нажатие на кнопку Оформить заказ')
    def click_on_order_button(self):
        self.click_on_item(MainPageLocators.ORDER_BUTTON)

    @allure.step('Нажатие на  ингредиент')
    def click_on_ingredient_bun(self):
        self.click_on_item(MainPageLocators.BUN_R2_D3_OBJECT)

    @allure.step('Отображение счётчика ингредиента')
    def get_ingredient_count(self):
        return self.item_text(MainPageLocators.BUN_COUNTER)

    @allure.step('Текст заголовка модального окна Детали ингредиента')
    def check_ingredient_details_label(self):
        return self.item_text(MainPageLocators.INGREDIENTS_DETAILS_LABEL)

    @allure.step('Закрытие модального окна Детали ингредиента')
    def close_ingredient_details(self):
        self.click_on_item(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step('Проверка закрытия модального окна Детали ингредиента')
    def check_invisibility_ingredient_details(self):
        self.check_invisibility(MainPageLocators.INGREDIENTS_DETAILS_LABEL)

    @allure.step('Перетаскивание ингредиента в заказ')
    def drag_and_drop_ingredient_in_order(self):
        self.drag_and_drop(MainPageLocators.BUN_R2_D3_OBJECT,
                           MainPageLocators.ORDER_AREA)

    @allure.step('Получение номера заказа')
    def get_number_for_order(self):
        self.waiting_for_item_to_be_visible(MainPageLocators.ORDER_NUMBER)
        self.check_invisibility(MainPageLocators.OVERLAY)
        return self.item_text(MainPageLocators.ORDER_NUMBER)

    @allure.step('Закрытие всплывающего окна с номером заказа')
    def close_order_window(self):
        self.check_invisibility(MainPageLocators.OVERLAY)
        self.click_on_item(MainPageLocators.CLOSE_ORDER_BUTTON)

    @allure.step('Создание полного заказа и получение его номера')
    def order_create(self):
        self.drag_and_drop_ingredient_in_order()
        self.click_on_order_button()
        self.check_invisibility(MainPageLocators.OVERLAY)
        number_for_order = self.get_number_for_order()
        self.close_order_window()
        return number_for_order

    @allure.step('Получение URL')
    def get_url_main_page(self):
        return self.driver.current_url
