Тестовое Задание

Реализовать 3 теста и придумать 1 свой (номер 4)
1. Зарегистрировать пользователя руками и на основании данных реализовать тест на проверку логина на сайт
2. Проверить переход и отображение товаров в каталоге(синяя кнопка сверху) Электроника -> Планшеты -> Digma
3. Проверка добавления товара в корзину и удаления из корзины

4. Проверка добавления товара в избранное и удаления из избранного
Все нужно закинуть в докер

----------------

запустить тесты: 

1 склонировать проект на локальный компьютер

2 добавить в проект .env файл с переменными окружения

3 установить зависимости 

``` pip install -r requirements.txt ```

4 запустить тесты локально

``` pytest -v ```

5 сборка образа и запуск тестов в docker

``` docker-compose up --build ```

----------------

