import allure

from data_to_use import TestData
from pages.login_page import LoginPage
from pages.pass_recovery_page import PassRecoveryPage


class TestPassRecovery:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_pass_recovery_correct_redirect(self, driver):
        driver.get(TestData.LOGIN_PAGE)
        login_page = LoginPage(driver)
        pass_recovery_page = PassRecoveryPage(driver)
        login_page.click_pass_recovery()
        expected_link = pass_recovery_page.get_url_recovery_page()
        assert expected_link == TestData.PASS_RECOVERY_PAGE

    @allure.title('Проверка сценария: Ввод email и клик на кнопку Восстановить')
    def test_add_email_and_click_recover_button(self, driver):
        driver.get(TestData.PASS_RECOVERY_PAGE)
        pass_recovery_page = PassRecoveryPage(driver)
        pass_recovery_page.email_input(TestData.EMAIL)
        pass_recovery_page.click_recovery_button()
        assert pass_recovery_page.check_for_enter_code_from_email_field() == 'Введите код из письма'

    @allure.title('Проверка, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_to_password_show(self, driver):
        driver.get(TestData.PASS_RECOVERY_PAGE)
        pass_recovery_page = PassRecoveryPage(driver)
        pass_recovery_page.email_input(TestData.EMAIL)
        pass_recovery_page.click_recovery_button()
        pass_recovery_page.click_to_show_password()
        assert pass_recovery_page.check_for_active_password_field()
