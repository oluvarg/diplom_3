
import allure

from pages.base_page import BasePage
from locators.recovery_locators import RecoveryLocators
from helper import helper_email, helper_password
from data import UrlsData


class RecoveryPasswordPage(BasePage):

    @allure.step('Открытие страницы "Восстановление пароля"')
    def open_forgot_password_page(self):
        self.open_url(UrlsData.FORGOT_PASSWORD)

    @allure.step('Получения заголовка')
    def check_title(self):
        return self.check_exist_element(RecoveryLocators.TITLE)

    @allure.step('Ввод данных в поле ввода "Email"')
    def input_email(self):
        self.set_text(RecoveryLocators.FILED_EMAIL, helper_email())

    @allure.step('Нажатие кнопки "Восстановить" ')
    def click_button_recovery(self):
        self.click_element_if_clickable(RecoveryLocators.BUTTON_RECOVERY)

    @allure.step('Проверка наличия поля ввода "Пароль"')
    def check_exist_field_password(self):
        return self.check_exist_element(RecoveryLocators.FIELD_PASSWORD)

    @allure.step('Ввода данных в поле "Пароль"')
    def input_password(self):
        self.set_text(RecoveryLocators.FIELD_PASSWORD, helper_password())

    @allure.step('Нажатие кнопки "Показать/скрыть"')
    def click_button_show_hide(self):
        self.click_element_if_clickable(RecoveryLocators.BUTTON_SHOW_HIDE)

    @allure.step('Получение статуса обводки поля ввода "Пароль"')
    def check_stroke_field_password(self):
        if self.find_element_visibility(RecoveryLocators.FIELD_ACTIVE_PASSWORD):
            return True

    @allure.step('Получение статуса поляв ввода "Пароль"')
    def check_activ_fild_password(self):
        if self.find_element_visibility(RecoveryLocators.FIELD_ACTIVE_PASSWORD):
            return True

    @allure.step('Предусловие для кнопки "Показать/скрыть"')
    def precondition_for_button_show_hide(self):
        self.open_forgot_password_page()
        self.input_email()
        self.click_button_recovery()
