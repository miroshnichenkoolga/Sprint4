from conftest import *
from selenium.webdriver.support import expected_conditions
import allure
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait


@allure.feature('Проверка раздела «Вопросы о важном» ')
class TestMainQuestionBlock:
    test_data = [
        [1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."],
        [2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать "
            "несколько заказов — один за другим."],
        [3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды "
            "начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, "
            "суточная аренда закончится 9 мая в 20:30."],
        [4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."],
        [5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."],
        [6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без "
            "передышек и во сне. Зарядка не понадобится."],
        [7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."],
        [8, "Да, обязательно. Всем самокатов! И Москве, и Московской области."]
    ]

    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description(
        'На главной странице перейти к разделу "Вопросы о важном", нажать на вопрос и проверить текст ответа')
    @pytest.mark.parametrize('number, answer_text', test_data)
    def test_check_answer_text(self, driver, number, answer_text):
        main_page = MainPage(driver)
        main_page.scroll_to_questions_section()
        main_page.click_question(number)
        main_page.check_answer(answer_text)
