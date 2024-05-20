from selenium.webdriver.common.by import By


class MainPageLocators:

    """ Заголовок "Соберите бургер" над конструктором """
    TITLE_CONSTRUCTOR = (By.XPATH, '//*[text() = "Соберите бургер"]')

    """ Кнопка "Конструктор" """
    BUTTON_CONSTRUCTOR = (By.XPATH, '//*[text() = "Конструктор"]')

    """ Кнопка "Лента Заказов" """
    BUTTON_ORDER_FEED = (By.XPATH, '//p[text()="Конструктор"]/parent::a')

    """ Кнопка булки "R2-D3" """
    BUTTON_INGREDIENT_R2_D3 = (By.XPATH, '//*[text()="Флюоресцентная булка R2-D3"]')

    """ Кнопка "Оформить заказ" """
    BUTTON_ORDER = (By.XPATH, '//*[text()="Оформить заказ"]')

    """ Текст "идентификатор заказа" """
    ID_ORDER_TEXT = (By.XPATH, '//p[text()="идентификатор заказа"]')

    """ Id оформленного заказа """
    ID_ORDER = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")

    """ Кнопка "Закрыть" """
    BUTTON_CLOSE = (By.XPATH, '//button[contains(@class,"close")]')

    """ Заголовок окна ингредиента """
    TITLE_INGREDIENT_WINDOW = (By.XPATH, '//*[text() = "Детали ингредиента"]')

    """ Счетчик у булки "R2-D3" """
    INGREDIENT_COUNTER = (By.XPATH, './/p[contains(@class, "counter_counter")]')

    """ Корзина заказов """
    BASKET_ORDER = (By.XPATH, '//*[@class="constructor-element__text" and text()="Перетяните булочку сюда (низ)"]')
