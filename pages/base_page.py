import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки объекта на странице')
    def waiting_for_item_to_be_visible(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности объекта на странице')
    def waiting_for_item_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Проверка присутствия элемента на странице')
    def check_visibility(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Проверка отсутствия элемента на странице')
    def check_invisibility(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.invisibility_of_element(locator))

    @allure.step('Клик на объект')
    def click_on_item(self, locator):
        self.waiting_for_item_to_be_clickable(locator)
        self.driver.find_element(*locator).click()

    @allure.step('Ввод какого-то значения в инпут поле')
    def set_value_for_input(self, locator, value):
        self.waiting_for_item_to_be_clickable(locator)
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('Посмотр какой текст отображается в необходимом объекте')
    def item_text(self, locator):
        self.waiting_for_item_to_be_visible(locator)
        return self.driver.find_element(*locator).text

    @allure.step('Drag and drop элемента')
    def drag_and_drop(self, locator_from, locator_to):
        self.waiting_for_item_to_be_visible(locator_from)
        self.waiting_for_item_to_be_visible(locator_to)
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        ActionChains(self.driver).drag_and_drop(element_from, element_to).perform()
