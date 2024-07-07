from selenium.webdriver.common.by import By


class PassRecoveryPageLocators:
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    RECOVERY_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')

    CODE_FROM_EMAIL_INPUT = (By.XPATH, '//label[text()="Введите код из письма"]')
    SHOW_PASSWORD_BUTTON = (By.XPATH, '//div[contains(@class,"icon-action")]')
    ACTIVE_PASS_INPUT = (By.XPATH, '//label[contains(@class,"input__placeholder-focused")]')
