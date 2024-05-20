import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators as LL
from data import UrlsData
import helper


class LoginPage(BasePage):

    @allure.step('Открытие страницы "Вход"')
    def open_login_page(self):
        self.open_url(UrlsData.LOGIN)

    @allure.step('Нажатие кнопки "Восстановить пароль" ')
    def click_recovery_password(self):
        self.click_element_if_clickable(LL.BUTTON_RECOVERY_PASSWORD)

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
