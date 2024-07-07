from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_HEADER = (By.XPATH, '//p[text()="Конструктор"]')
    ORDER_FEED_HEADER = (By.XPATH, '//p[text()="Лента Заказов"]')
    PERSONAL_ACCOUNT_HEADER = (By.XPATH, '//p[text()="Личный Кабинет"]')

    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')
    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    BUN_R2_D3_OBJECT = (By.XPATH, '//ul[contains(@class,"BurgerIngredients_ingredients__list")][1]/a[1]')
    BUN_COUNTER = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[contains(@class, "counter__num")]')

    INGREDIENTS_DETAILS_LABEL = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    CLOSE_INGREDIENT_DETAILS_BUTTON = (By.XPATH, '//section[1]//div[1]//button[contains(@class,'
                                                 '"Modal_modal__close_modified")]')

    ORDER_AREA = (By.XPATH, '//section[contains(@class,"BurgerConstructor_basket")]')
    ORDER_NUMBER = (By.XPATH, '//*[contains(@class, "type_digits-large")]')
    ORDER_STATUS_TEXT = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')
    CLOSE_ORDER_BUTTON = (By.XPATH, '//button[contains(@class,"Modal_modal__close")]')
    OVERLAY = (By.XPATH, '//div/div[@class="Modal_modal_overlay__x2ZCr"]')
