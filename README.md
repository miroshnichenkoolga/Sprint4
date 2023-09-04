### Приложение Яндекс.Самокат». С помощью приложения можно заказать самокат: выбрать адрес доставки, число, кол-во суток, цвет самоката.
### Подключен Selenium и Allure
### Приложение необходимо проверить в браузере Mozilla Firefox
### Написана функция, которая генерирует логины (имя, фамилию и номер телефона).
### Для тестов применен Page Object Model 
### Использована параметризация для блока "Вопросы о важном"

### Тестовые сценарии
#### Создан заказ, заполнена форма заказа.
#### Проверено всплывающее окно с сообщением об успешном создании заказа.
#### Проверено, что если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».
#### Проверено, что если нажать на логотип «Яндекса», попадёшь на страницу Яндекс Дзен.
#### Тест на блок "Вопросы о важном" один параметризованный. На вход принимает локатор вопроса, локатор ответа, текст ответа
 