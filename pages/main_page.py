import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from faker import Faker
from selenium.webdriver.common.by import By
import datetime


class MainPage(BasePage):
    button_order_near_order_status = [By.XPATH, '//div[@class="Header_Nav__AGCXC"]/child::button']
    button_order_near_question_block = [By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/child::button']
    logo_scot = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    logo_yandex = [By.XPATH, '//a[@href="//yandex.ru"]']
    questions_section_head = [By.XPATH, './/div[text()="Вопросы о важном"]']
    questions = [By.CLASS_NAME, 'accordion__heading']
    visible_answer = [By.XPATH, './/div[contains(@class, "accordion__panel") and not(@hidden)]']

    @allure.step('Прокрутить страницу до раздела "Вопросы о важном"')
    def scroll_to_questions_section(self):
        questions_section = self.find_element(self.questions_section_head)
        self.execute_script_scroll(questions_section)

    @allure.step('Нажать на вопрос номер {number}')
    def click_question(self, number):
        questions = self.find_elements(self.questions)
        self.wait_visibility_of_element_located(self.questions)
        questions[number - 1].click()

    @allure.step('Проверить что открывшийся текст ответа совпадает с ожидаемым')
    def check_answer(self, text_answer):
        self.wait_visibility_of_element_located(self.visible_answer)
        assert self.find_element(self.visible_answer).text == text_answer

    @allure.step('Поиск кнопки "Заказать" и клик по ней')
    def select_click_button_order_near_order_status(self):
        self.find_element(self.button_order_near_order_status).click()

    @allure.step('Клик на лого "Самокат"')
    def check_click_on_logo_scot(self):
        self.wait_element_to_be_clickable(self.logo_scot).click()
        self.wait_visibility_of_element_located(self.button_order_near_order_status)
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.step('Клик на лого "Яндекс"')
    def check_click_on_logo_yandex(self):
        self.find_element(self.logo_yandex).click()
        self.switch_to_window()
        link = 'https://dzen.ru/?yredirect=true'
        url_yandex = 'yandex.ru'
        timeout = 5
        current_link = self.get_url_waiting(timeout, link, url_yandex)
        assert current_link == 'https://dzen.ru/?yredirect=true'

