import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Ввод email-а')
    def email_input(self, email):
        self.set_value_for_input(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step('Ввод пароля')
    def input_password(self, password):
        self.set_value_for_input(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step('Нажатие на кнопку Войти')
    def click_log_in(self):
        self.click_on_item(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Нажатие на кнопку Восстановить пароль')
    def click_pass_recovery(self):
        self.click_on_item(LoginPageLocators.PASS_RECOVERY_HREF)
