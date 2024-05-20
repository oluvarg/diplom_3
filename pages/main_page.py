import allure

from pages.base_page import BasePage
from data import UrlsData
from locators.main_page_locators import MainPageLocators as MPL


class MainPage(BasePage):

    @allure.step('Открытие страницы регистрации')
    def open_reg_page(self):
        self.open_url(UrlsData.REGISTER)

    @allure.step('Открытие главной страницы')
    def open_main_page(self):
        self.open_url(UrlsData.MAIN_PAGE)

    @allure.step('Нажатие на кнопку "Конструктор"')
    def click_button_constructor(self):
        self.click_element_if_clickable(MPL.BUTTON_CONSTRUCTOR)

    @allure.step('Нажатие на кнопку "Лента Заказов"')
    def click_button_order_feed(self):
        self.click_element_if_clickable(MPL.BUTTON_ORDER_FEED)

    @allure.step('Проверка открытия страницы после нажатия на кнопку "Конструктор"')
    def check_title_constructor(self):
        return self.check_exist_element(MPL.TITLE_CONSTRUCTOR)

    @allure.step('Нажатие на кнопку булки "R2-D3"')
    def click_button_ing_r3_d3(self):
        self.click_element_if_clickable(MPL.BUTTON_INGREDIENT_R2_D3)

    @allure.step('Проверка открытия окна ингредиента')
    def check_clickable_order_button(self):
        if self.find_element_clickable(MPL.BUTTON_ORDER_FEED):
            return True
        else:
            return False

    @allure.step('Нажатие на крестик в окне ингредиента')
    def click_close_button(self):
        self.click_element_if_clickable(MPL.BUTTON_CLOSE)

    @allure.step('Предусловие: открытие главной страницы, открытие окна ингредиента')
    def precondition_close_window(self):
        self.open_main_page()
        self.click_button_ing_r3_d3()

    @allure.step('Получение значения счетчика ингредиента')
    def get_count_value(self):
        return self.get_text(MPL.INGREDIENT_COUNTER)

    @allure.step('Перетаскивание ингредиента')
    def add_filling_to_order(self):
        self.find_element_clickable(MPL.BUTTON_INGREDIENT_R2_D3)
        self.drag_and_drop_on_element(MPL.BUTTON_INGREDIENT_R2_D3, MPL.BASKET_ORDER)

    @allure.step('Нажатие на кнопку "Оформить заказ"')
    def click_order_button(self):
        self.click_element_if_clickable(MPL.BUTTON_ORDER)

    @allure.step('Получение текста из окна с информацией о только что оформленном заказе')
    def check_placing_order(self):
        self.find_element_visibility(MPL.ID_ORDER_TEXT)
        return self.get_text(MPL.ID_ORDER_TEXT)

    @allure.step('Получение id заказа')
    def get_order_id(self):
        self.find_element_visibility(MPL.ID_ORDER_TEXT)
        order_id = self.get_text(MPL.ID_ORDER)
        while order_id == '9999':
            order_id = self.get_text(MPL.ID_ORDER)
        return f"{order_id}"

    @allure.step("Закрытие окна после создания заказа")
    def click_close_window_order(self):
        self.find_element_clickable(MPL.BUTTON_CLOSE)
        self.click_element_if_clickable(MPL.BUTTON_CLOSE)
