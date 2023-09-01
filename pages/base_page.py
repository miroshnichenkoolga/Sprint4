import allure
from faker import Faker
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:


    def __init__(self, driver):
        self.driver = driver
        self.faker = Faker(locale="ru_RU")

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Поиск элементов')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Подождать пока элемент станет кликабельным')
    def wait_element_to_be_clickable(self, locator, time=1):
        return WebDriverWait(self.driver, time) \
            .until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Подождать загрузки страницы')
    def wait_visibility_of_element_located(self, locator, time=3):
        WebDriverWait(self.driver, time) \
            .until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Получаем текущий  current_url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Выполнить script')
    def execute_script_scroll(self, questions_section):
        self.driver.execute_script('arguments[0].scrollIntoView();', questions_section)

    @allure.step('Переключиться на окно')
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Ожидание получения текущего url"')
    def get_url_with_waiting(self, timeout=3):
        WebDriverWait(self.driver, timeout).until(EC.any_of(EC.url_to_be('https://dzen.ru/?yredirect=true'), EC.url_contains('yandex.ru')))
        return self.driver.current_url