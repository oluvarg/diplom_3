import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators as LL
from data import UrlsData


class LoginPage(BasePage):

    @allure.step('Открытие страницы "Вход"')
    def open_login_page(self):
        self.open_url(UrlsData.LOGIN)

    @allure.step('Нажатие кнопки "Восстановить пароль" ')
    def click_recovery_password(self):
        self.click_element_if_clickable(LL.BUTTON_RECOVERY_PASSWORD)
