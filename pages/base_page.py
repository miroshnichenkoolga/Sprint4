import allure
from faker import Faker
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.common.by import By
from conftest import *

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

