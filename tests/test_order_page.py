import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from conftest import *
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestOrderPage:

    driver = None

    @allure.title('Проверка клика по кнопке "Заказать" в верху страницы')
    @allure.description('На странице ищем кнопку "Заказать", производим клик и проверяем, что current_url == '
                        '"https://qa-scooter.praktikum-services.ru/order"')
    def test_go_to_order_page_from_mane(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.select_click_button_order_near_order_status()
        order_page.check_go_to_order_page_from_mane()

    @allure.title('Проверка создания нового заказа')
    @allure.description('Создаем новый заказ и проверяем, что появляется сообщение "Заказ оформлен" с номером заказа')
    def test_create_new_order(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.select_click_button_order_near_order_status()
        order_page.select_create_new_order_who_is_the_scot_for()
        order_page.select_create_new_order_about_rent()
        order_page.check_pop_up_window_when_create_new_order()



