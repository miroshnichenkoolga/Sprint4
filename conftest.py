import allure
import pytest
from selenium import webdriver

url = 'https://qa-scooter.praktikum-services.ru/'

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(url)
    yield driver
    driver.quit()
