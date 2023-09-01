from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.common.by import By
import datetime
from pages.base_page import BasePage


class OrderPage(BasePage):
    url_page = 'https://qa-scooter.praktikum-services.ru/order'
    button_further = [By.XPATH, '//button[text()="Далее"]']
    order_header = [By.XPATH, '//div[text()="Для кого самокат"]']
    field_name = [By.XPATH, '//input[@placeholder ="* Имя"]']
    field_last_name = [By.XPATH, '//input[@placeholder ="* Фамилия"]']
    field_address = [By.XPATH, '//input[@placeholder ="* Адрес: куда привезти заказ"]']
    field_metro_station = [By.XPATH, '//input[@placeholder ="* Станция метро"]']
    field_phone = [By.XPATH, '//input[@placeholder ="* Телефон: на него позвонит курьер"]']
    field_when_bring_scot = [By.XPATH, '//input[@placeholder ="* Когда привезти самокат"]']
    field_rental_period = [By.XPATH, '//div[text()="* Срок аренды"]']
    check_box_color_scot = [By.XPATH, '//div[text()="Цвет самоката"]']
    button_order = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/child::button [text()="Заказать"]']
    two_day_rent_period = [By.XPATH, '//div[text()="двое суток"]']
    button_yes_wont_create_order = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/child::button [text()="Да"]']
    button_back = [By.XPATH, '//button[text()="Назад"]']
    check_box_black_scot = [By.ID, 'black']
    pop_up_wind_create_order = [By.XPATH, '//div[text()="Заказ оформлен"]']
    button_view_status = [By.XPATH,
                          '//div[@class="Order_NextButton__1_rCA"]/child::button [text()="Посмотреть статус"]']
    massage_enter_valid_name = [By.XPATH, '//div[@class="Input_InputContainer__3NykH"]/child::div[text()="Введите '
                                          'корректное имя"]']
    locator_body =[By.TAG_NAME, "body"]
    metro_station = [By.CLASS_NAME, "select-search__row"]
    window_create_order = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']

    @allure.step('Заполнить поле "Имя"')
    def set_name(self):
        self.find_element(self.field_name).send_keys(self.faker.first_name())

    @allure.step('Заполнить поле "Фамилия"')
    def set_last_name(self):
        self.driver.find_element(*self.field_last_name).send_keys(self.faker.last_name())

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self):
        self.driver.find_element(*self.field_address).send_keys("Жуковского 45")

    @allure.step('Заполнить поле "Телефон"')
    def set_phone(self):
        new_phone = self.rnd_phone_number()
        self.driver.find_element(*self.field_phone).send_keys(new_phone)

    def rnd_phone_number(self):
        r = "8"
        for i in range(10):
            r += str(self.faker.pyint(0, 9))
        return r

    @allure.step('Задано ожидание, кнопка "Далее" станет кликабельной')
    @allure.step('Получаем текущий  current_url и сравниваем с url_page')
    def check_go_to_order_page_from_mane(self):
        self.wait_element_to_be_clickable(self.button_further, 1)
        assert self.get_current_url() == self.url_page

    @allure.step('Заполнить поля формы "Для кого самокат"')
    def select_create_new_order_who_is_the_scot_for(self):
        self.wait_element_to_be_clickable(self.button_further)
        self.set_name()
        self.set_last_name()
        self.set_address()
        self.find_element(self.field_metro_station).click()
        els = self.find_elements(self.metro_station)
        els[0].click()
        self.set_phone()
        self.find_element(self.button_further).click()

    @allure.step('Заполнить поля формы "Про аренду"')
    def select_create_new_order_about_rent(self):
        d = datetime.date.today().strftime("%d.%m.%y")
        self.wait_element_to_be_clickable(self.field_when_bring_scot).send_keys(d)
        self.find_element(self.locator_body).click()
        self.find_element(self.field_rental_period).click()
        self.find_element(self.two_day_rent_period).click()
        self.find_element(self.check_box_black_scot).click()
        self.find_element(self.button_order).click()
        self.find_element(self.button_yes_wont_create_order).click()

    @allure.step('Получить текст всплывающего окна "Заказ оформлен"')
    def check_pop_up_window_when_create_new_order(self):
        assert "Заказ оформлен" in self.find_element(self.window_create_order).text


