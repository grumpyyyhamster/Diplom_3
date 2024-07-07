from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    ORDER_HISTORY = (By.XPATH, '//a[text()="История заказов"]')
    LOGOUT = (By.XPATH, '//button[text()="Выход"]')

    LAST_ORDER = (By.XPATH, '//li[last()]/a/div[1]/p[1]')
