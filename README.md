# online-store — интернет магазин (В РАЗРАБОТКЕ)

## Описание:

`_Раздел дорабатывается_`

## Установка:

Рекомендуется использовать PyCharm

Ссылка для добавления проекта
[git@github.com:kirillbarkhatov/online_store.git]()

Для создания виртуального окружения и установки зависимостей используйте Poetry

`_Раздел дорабатывается_`

## Использование:

В настоящее время доступ к функционалу из единой точки входа не реализован

Для запуска web-сервера запустите модуль `web`

`_Раздел дорабатывается_`

## Функционал

Функционал разбит модули:
1. `utils`
2. `category`
3. `product`
4. `product_iterator`
5. `smartphone`
6. `lawn_grass`
7. `base_product`
8. `order`
9. `print_mixin`
10. `exceptions`
11. `web`


Поддерживается чтение данных о транзакциях из файлов формата `json`

Модули `category` и `product` содержат описания классов, а также методы, геттеры и сетторы для работы с ними

Модули `smartphone` и `lawn_grass` содержат классы-наследники от класса `Product`

Модуль `base_product` содержит абстрактный класс для всех продуктов

Модуль `print_mixin` содержит миксин класс для вывода в консоль информации о созданном объекте 

В модуле `product_iterator` содержится класс, позволяющий создать итератор продуктов заданной категории

В модуле `exceptions` описаны кастомные исключения

В модуле `web` реализован веб-сервер

## Тестирование:

Код в модулях пакета `src/` покрыт тестами
Для запуска тестов используйте команду `pytest`

Для проверки покрытия тестами используйте команду `pytest --cov`
Для генерации отчета по тестам в html используйте команду `pytest --cov --cov-report=html`


## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE)