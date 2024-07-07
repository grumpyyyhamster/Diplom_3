import allure

from locators.login_page_locators import LoginPageLocators
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    @allure.step('Нажатие на кнопку История заказов')
    def click_on_order_history(self):
        self.click_on_item(PersonalAccountPageLocators.ORDER_HISTORY)

    @allure.step('Нажатие на кнопку Выход')
    def click_logout(self):
        self.click_on_item(PersonalAccountPageLocators.LOGOUT)
        self.waiting_for_item_to_be_visible(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Получение номера последнего заказа')
    def get_number_last_order(self):
        return self.item_text(PersonalAccountPageLocators.LAST_ORDER)

    @allure.step('Получение URL')
    def get_url_personal_account_page(self):
        return self.driver.current_url
