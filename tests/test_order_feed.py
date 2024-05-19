import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage


class TestOrderFeed:

    @allure.title('Проверка открытия окна с информацией заказе')
    def test_open_order_window(self, driver):
        ofp = OrderFeedPage(driver)
        ofp.open_page()
        ofp.click_order()
        return ofp.check_order_window() is True, 'Окно не открыто'

    @allure.title('Проверка совпадения id в ленте заказов и в истории заказов')
    def test_find_order_in_list(self, driver):
        pp = ProfilePage(driver)
        ofp = OrderFeedPage(driver)
        mp = MainPage(driver)

        pp.authorization()
        mp.add_filling_to_order()
        mp.click_order_button()
        order_id = mp.get_order_id
        mp.click_close_window_order()
        pp.open_profile_page()
        pp.open_history_page()
        order_id_history = pp.found_order_at_history(order_id)
        mp.click_button_order_feed()

        order_id_order_feed = ofp.found_order_at_feed(order_id)
        assert order_id_order_feed and order_id_history is True, 'Id не совпадают'

    @allure.title('Проверка изменения счетчика заказов за сегодня')
    def test_today_orders_counter(self, driver):
        pp = ProfilePage(driver)
        ofp = OrderFeedPage(driver)
        mp = MainPage(driver)

        pp.authorization()
        mp.click_button_order_feed()
        pre_count = ofp.get_total_count_today()
        mp.click_button_constructor()
        mp.add_filling_to_order()
        mp.click_order_button()
        mp.click_close_window_order()
        mp.click_button_order_feed()
        post_count = ofp.get_total_count_today()
        assert post_count > pre_count, 'Счетчик не изменился'

    @allure.title('Проверка появления только что созданного заказа в ленте заказов')
    def test_new_order_at_order_feed(self, driver):
        pp = ProfilePage(driver)
        ofp = OrderFeedPage(driver)
        mp = MainPage(driver)

        pp.authorization()
        mp.add_filling_to_order()
        mp.click_order_button()
        order_id = mp.get_order_id
        mp.click_close_window_order()
        mp.click_button_order_feed()
        assert ofp.found_order_at_feed(order_id) is True

