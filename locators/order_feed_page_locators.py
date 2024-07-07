from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    LAST_ORDER = (By.XPATH, '//li[contains(@class,"OrderHistory")][1]')
    ORDER_DETAILS = (By.XPATH, '//section[contains(@class,"Modal_modal_opened")]//div['
                               'contains(@class,"Modal_modal__container")]')

    ORDER_FEED_LIST = (By.XPATH, '//ul[@class="OrderFeed_orderList__cBvyi"]//li')
    ORDER_IN_PROGRESS_NUMBER = (
        By.XPATH, '//*[contains(@class,"orderListReady")]//li[contains(@class,"digits-default")]')

    ORDERS_FOR_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,'
                                     '"OrderFeed_number")]')
    ORDERS_FOR_TODAY = (By.XPATH,
                        '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"OrderFeed_number")]')
