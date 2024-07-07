import allure

from locators.pass_recovery_page_locators import PassRecoveryPageLocators
from pages.base_page import BasePage


class PassRecoveryPage(BasePage):

    @allure.step('Ввод email')
    def email_input(self, email):
        self.set_value_for_input(PassRecoveryPageLocators.EMAIL_INPUT, email)

    @allure.step('Нажатие на кнопку Восстановить')
    def click_recovery_button(self):
        self.click_on_item(PassRecoveryPageLocators.RECOVERY_BUTTON)

    @allure.step('Проверка поля Ввести код из письма')
    def check_for_enter_code_from_email_field(self):
        return self.item_text(PassRecoveryPageLocators.CODE_FROM_EMAIL_INPUT)

    @allure.step('Нажатие на кнопку отображения пароля')
    def click_to_show_password(self):
        self.click_on_item(PassRecoveryPageLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Проверка активности поля Пароль')
    def check_for_active_password_field(self):
        return self.check_visibility(PassRecoveryPageLocators.ACTIVE_PASS_INPUT)

    @allure.step('Получение URL')
    def get_url_recovery_page(self):
        return self.driver.current_url
