import allure
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage


class TestProfile:

    @allure.title('Открытие страницы "Личный кабинет"')
    def test_open_profile_page(self, driver):
        pp = ProfilePage(driver)
        lp = LoginPage(driver)
        lp.authorization()
        pp.open_profile_page()
        assert pp.check_open_page() is True

    @allure.title('Переход на страницу "История заказов"')
    def test_open_history(self, driver):
        pp = ProfilePage(driver)
        lp = LoginPage(driver)
        lp.authorization()
        pp.open_profile_page()
        assert pp.open_history_page() is True

    @allure.title('Проверка выхода пользователя при нажатие на кнопку "Выйти"')
    def test_exit(self, driver):
        pp = ProfilePage(driver)
        lp = LoginPage(driver)
        lp.authorization()
        pp.open_profile_page()
        assert pp.exit() is True
