from conftest import *
from selenium.webdriver.support import expected_conditions
import allure
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait


@allure.feature('Проверка тестовых ссылок')
class TestLinks:

    @allure.title('Проверка клика на логотип «Самоката»')
    @allure.description('При помощи клика по кнопке "Заказать" переходим в форму заказа и кликаем на лого "Самокат", '
                        'проверяем current_url == "https://qa-scooter.praktikum-services.ru/"')
    def test_click_on_logo_scot(self, driver):
        main_page = MainPage(driver)
        main_page.select_click_button_order_near_order_status()
        main_page.check_click_on_logo_scot()

    @allure.title('Проверка перехода на главную страницу Яндекс.дзен по клику на лого "Яндекс"')
    @allure.description('Находясь на странице заказа, нажать на лого "Яндекс" и убедиться, что произошел переход на '
                        'главную страницу Яндекс.дзен')
    def test_click_on_logo_yandex_open_new_wind(self, driver):
        main_page = MainPage(driver)
        main_page.check_click_on_logo_yandex()

