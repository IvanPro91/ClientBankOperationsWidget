# Виджет банковских операций клиента.

![SkyPro](https://my.sky.pro/5987ea2b7acbe5e5379157f8c4f0fb7f.svg)
## Цель проекта
>Целью проекта является оценка навыков Junior программиста на данном этапе написания домашней работы

## Описание проекта
>Виджет для личного кабинета клиента крупного банка.
Виджет, который показывает несколько последних успешных банковских операций клиента.

# Доступные модули и методы
* Модуль masks.py
* Модуль widget.py
* Модуль processing.py
* Модуль generators.py
* Модуль external_api.py
* Модуль utils.py
* Модуль finance.py
* Модуль find_word_regular.py

## Модуль masks.py
Модуль для маскировки номера пользовательского счета или счета в банке

## Методы

| Метод            | Аргументы                        |  Возвращаемый тип | Описание                                                              |
|------------------|----------------------------------|-------------------|-----------------------------------------------------------------------|
| account_card     | ```card_number``` str: Строка    | str: Строка       | Функция преобразования номера карты в маску вида XXXX XX** **** XXXX  |
| get_mask_account | ```number_account``` str: Строка | str: Строка       | Функция преобразования номера счета в нужный формат маскировки **XXXX |

## Модуль widget.py
Модуль получения типа и номера карты/счета, а так-же преобразования даты в формат ДД.ММ.ГГГГ с ISO формата даты и времени

## Методы

| Метод             | Аргументы                     | Возвращаемый тип   | Описание                                                                            |
|-------------------|-------------------------------|--------------------|-------------------------------------------------------------------------------------|
| mask_account_card | ```card_number``` str: Строка | str: Строка        | Функция получения типа и номера карты или счета пример Visa Plantum XXXX, Счет XXXX |
| get_date          | ```date``` str: Строка        | str: Строка        | Функция преобразования даты в нужный формат с помощью datetima                      |

## Модуль processing.py
Модуль работы со списком словарей и опциональными значениями для ключа и сортировки

## Методы

| Метод             | Аргументы                                                                              | Возвращаемый тип               | Описание                                                                                                                       |
|-------------------|----------------------------------------------------------------------------------------|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| filter_by_state   | ```list_data``` тип list[dict]: Список словарей<br/>```state``` тип str: Строка        | list[dict]: Список словарей    | Функция возвращает новый список словарей, содержащий только те словари,у которых ключ state соответствует указанному значению. |
| sort_by_date      | ```list_data``` тип list[dict]: Список словарей<br/>```sort_reverse``` тип str: Строка | list[dict]: Список словарей    | Функция возвращает новый список, отсортированный по дате (date).                                                               |


## Модуль generators.py
Модуль эффективной работы с большими объемами данных транзакций, используя возможности Python для обработки данных через генераторы.

## Методы

| Метод                    | Аргументы                                                                          | Возвращаемый тип                  | Описание                                                   |
|--------------------------|------------------------------------------------------------------------------------|-----------------------------------|------------------------------------------------------------|
| filter_by_currency       | ```list_data``` тип list[dict]: Список словарей<br/>```currency``` тип str: Строка | Iterator[dict]: Итератор словарей | Функция фильтрует по ключу currency в списке словарей      |
| transaction_descriptions | ```list_data``` тип list[dict]: Список словарей                                    | Generator: Генератор              | Функция описания каждой транзакции переданного в аргументе |
| card_number_generator    | ```start``` тип int: Цифра<br/>```stop``` тип int: Цифра                           | list: Список                      | Функция генерирует номера карт                             |

## Модуль external_api.py
Модуль для конвертации валют с помощью API

## Методы
| Метод                    | Аргументы                         | Возвращаемый тип                | Описание                                         |
|--------------------------|-----------------------------------|---------------------------------|--------------------------------------------------|
| convert_currency         | ```dict_data``` тип dict: Словарь | float: Число с плавающей точкой | ункция конвертации валюты из USD и EUR в рубли.  |


## Модуль utils.py
Модуль для чтения файла json

## Методы
| Метод                    | Аргументы                      | Возвращаемый тип | Описание                   |
|--------------------------|--------------------------------|------------------|----------------------------|
| read_json_file           | ```filename``` тип str: Строка | list: Лист       | Функция чтения JSON-файла  |


## Модуль finance.py
Модуль для чтения файлов формата csv и excel финансовых операций

## Методы
| Метод                                  | Аргументы                                                       | Возвращаемый тип                      | Описание                                                                                   |
|----------------------------------------|-----------------------------------------------------------------|---------------------------------------|--------------------------------------------------------------------------------------------|
| read_finance_csv_operation             | ```filename``` тип str, None: Строка(Необязательный аргумент)   | list[dict[Any, Any]]: Лист словарей   | Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями.   |
| read_finance_excel_operation           | ```filename``` тип str, None: Строка(Необязательный аргумент)   | list[dict[Any, Any]]: Лист словарей   | Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями. |

## Модуль find_word_regular.py
Модуль для поиска по ключевому слову и подчет количества групп

## Методы
| Метод                        | Аргументы                                                                            | Возвращаемый тип          | Описание                                                       |
|------------------------------|--------------------------------------------------------------------------------------|---------------------------|----------------------------------------------------------------|
| filter_by_word               | ```transaction``` тип list[dict]: Список словарей<br>```word``` тип str: Строка      | list[dict]: Лист словарей | Функция поиска по регулярному выражению в описании транзакции. |
| count_all_by_category        | ```transaction``` тип list[dict]: Список словарей<br>```category``` тип list: Список | dict: Cловарь             | Функция подчета количества операций по категориям.             |

# Декораторы.
## Модуль decorators.py
## Декоратор ```log```
Декоратор, принимающий на вход необязательный аргумент filename, при успешном или ошибочном выполнении функции, декоратор запишет или выведет в консоль результат, вывод зависит от аргумента filename

### Структура декоратора
* ```log(filename: Any = None)``` - filename - необязательный аргумент
* ```log_decorator(func: Any)``` - func - принимающая функция на вход
* ```wrapper(*args: Any, **kwargs: Any)``` - функция выполняющая логику


# Тестирование
### Модуль masks

1. Функция ```get_mask_card_number```:
- Тестирование правильности маскирования номера карты.
- Проверка работы функции на различных входных форматах номеров карт, включая граничные случаи и нестандартные длины номеров.
- Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.

2. Функция ```get_mask_account```:
- Тестирование правильности маскирования номера счета.
- Проверка работы функции с различными форматами и длинами номеров счетов.
- Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины.

### Модуль widget
1. Функция ```mask_account_card```:
- Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).
- Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
- Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.

2. Функция ```get_date```:
- Тестирование правильности преобразования даты.
- Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
- Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.

### Модуль processing
1. Функция ```filter_by_state```:
- Тестирование фильтрации списка словарей по заданному статусу ```state```.
- Проверка работы функции при отсутствии словарей с указанным статусом ```state``` в списке.
- Параметризация тестов для различных возможных значений статуса ```state```.

2. Функция ```sort_by_date```:
- Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
- Проверка корректности сортировки при одинаковых датах.
- Тесты на работу функции с некорректными или нестандартными форматами дат.

### Модуль generators
1. Функция ```filter_by_currency```:
- Тесты, проверяющие, что функция корректно фильтрует транзакции по заданной валюте.
- Функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют.
- Генератор не завершается ошибкой при обработке пустого списка или списка без соответствующих валютных операций.

2. Функция ```transaction_descriptions```:
- Функция возвращает корректные описания для каждой транзакции.
- Работа функции с различным количеством входных транзакций, включая пустой список.

3. Функция ```card_number_generator```:
- Тесты, которые проверяют, что генератор выдает правильные номера карт в заданном диапазоне.
- Корректность форматирования номеров карт.
- Генератор корректно обрабатывает крайние значения диапазона и правильно завершает генерацию.

### Модуль decorators
Тестирование декоратора ```log```
* Тестирование вывода в консоль было с помощью ```capsys```
* Тестирование вывода в файл было реализовано отдельно.

### Модуль utils
* Тестирование наличия файла(пути файла)
* Тестирование отсутствия файла(пути файла)

### Модуль finance
* Тестирование с помощью patch функции read_finance_csv_operation и на ошибку
* Тестирование с помощью Mock() функции read_finance_excel_operation и на ошибку

### Модуль external_api
Тестирование модуля производилось с помощью Mock и patch из стандартной библиотеки python
* Тестирование на наличие кода отличавшегося от RUB
* Тестирование если данных нет на входе
* Тестирование если данные равны коду транзакции RUB

### Модуль find_word_regular
Тестирование модуля производилось с помощью фикстур
* Тестирование на поиск по регулярному выражению
* Тестирование на корректный подчет искомых категорий

### Общие аспекты тестирования
- Фикстуры. Для всех тестов создайте фикстуры, которые предоставят тестовые данные для списков словарей, включая различные случаи и комбинации state и date.
- Покрытие тестами. Убедитесь, что все ветви кода и исключения, которые могут быть сгенерированы вашими функциями, тестируются.
- Mock()
- patch

### Logging
Добавлен процесс записи информации о том, что происходит в программе во время ее работы.
* Добавлено логирование модуля utils при успешном завершении функции
* Добавлено логирование модуля masks при успешном завершении функции

# Установка
> Для начала работы с проектом выполните следующие шаги:

### Клонирование репозитория
Склонируйте репозиторий на ваш компьютер

```git clone git@github.com:IvanPro91/homework_skypro.git```

### Установка Poetry
Если у вас еще не установлен Poetry, выполните следующую команду указанную на официальном сайте
[Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)

После установки добавьте [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) в PATH, если это не произошло автоматически:

```export PATH="$HOME/.local/bin:$PATH"```

### Установка зависимостей
Используйте [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) для создания виртуального окружения и установки 
зависимостей (включая инструменты для разработки, 
такие как flake8, isort, black и mypy):

poetry install

### Активация виртуального окружения
**Активируйте виртуальное окружение [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) в зависимости от версии**

# Лицензия
MIT
