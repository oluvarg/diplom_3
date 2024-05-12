
import allure

import helper
from data import UrlsData
from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators as PL
from locators.login_locators import LoginLocators as LL


class ProfilePage(BasePage):

    @allure.step('Открытие страницы')
    def open_profile_page(self):
        self.find_element_visibility(PL.BUTTON_PROFILE_PAGE)
        self.click_element_if_clickable(PL.BUTTON_PROFILE_PAGE)

    @allure.step('Проверка наличия элементов на открытой странице')
    def check_open_page(self):
        self.find_element_visibility(PL.BUTTON_PROFILE)
        return self.check_exist_element(PL.BUTTON_PROFILE)

    @allure.step('Открытие страницы "История заказов"')
    def open_history_page(self):
        self.find_element_visibility(PL.BUTTON_HISTORY)
        self.click_element_if_clickable(PL.BUTTON_HISTORY)
        if self.get_url() == UrlsData.HISTORY_PAGE:
            return True
        else:
            return False

    @allure.step("Проверка нахождение идентификатора заказа в истории")
    def found_order_at_history(self, order_id):
        elements = self.find_until_all_elements_located(PL.ORDERS_AT_HISTORY)

        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.step('Нажатие кнопки "Выход"')
    def exit(self):
        self.find_element_visibility(PL.BUTTON_EXIT)
        self.click_element_if_clickable(PL.BUTTON_EXIT)
        self.find_element_not_visibility(PL.BUTTON_EXIT)
        if self.get_url() == UrlsData.LOGIN:
            return True
        else:
            return False

    @allure.step('Авторизация')
    def authorization(self):
        name = helper.helper_name()
        password = helper.helper_password()
        email = helper.helper_email()

        self.open_url(UrlsData.REGISTER)
        self.find_element_visibility(LL.FIELD_NAME_FOR_REG)

        self.set_text(LL.FIELD_NAME_FOR_REG, name)
        self.set_text(LL.FIELD_EMAIL_FOR_REG, email)
        self.set_text(LL.FIELD_PASSWORD_FOR_REG, password)

        self.click_element_if_clickable(LL.BUTTON_FOR_REG)
        self.find_element_not_visibility(LL.BUTTON_FOR_REG)

        self.find_element_visibility(LL.FIELD_EMAIL_FOR_LOGIN)
        self.set_text(LL.FIELD_EMAIL_FOR_LOGIN, email)
        self.set_text(LL.FIELD_PASSWORD_FOR_LOGIN, password)

        self.click_element_if_clickable(LL.BUTTON_FOR_LOGIN)
        self.find_element_not_visibility(LL.BUTTON_FOR_LOGIN)

    def precondition_for_tests(self):
        self.authorization()
        self.open_profile_page()
