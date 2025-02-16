from typing import Generator, Iterator


def filter_by_currency(list_data: list[dict], currency: str) -> Iterator[dict]:
    """
    Функция фильтрует по ключу currency в списке словарей
    :param list_data: Список словарей
    :param currency: Аргумент фильтра
    :return: Отфильтрованный генератор
    """
    if len(list_data) == 0:
        raise ValueError("Error length 'list_data'")
    if len(currency) == 0:
        raise ValueError("Error no data in 'currency'")
    c_generator = (
        transaction for transaction in list_data if transaction["operationAmount"]["currency"]["code"] == currency
    )
    return c_generator


def transaction_descriptions(list_data: list[dict]) -> Generator:
    """
    Функция описания каждой транзакции переданного в аргументе
    :param list_data: Список словарей
    :return: Генератор с описанием транзакции
    """
    print(len(list_data))
    if len(list_data) == 0:
        raise ValueError("Error length 'list_data'")

    for transaction in list_data:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> list:
    """
    Функция генерирует номера карт
    :param start: Число начала генерации
    :param stop: Число окончания генерации
    :return: Список сгенерированных номеров
    """
    if start == stop:
        raise ValueError("Warning, arg `start` equals arg `stop`")

    result = []
    for i_range in range(start, stop):
        zfill_res = str(i_range).zfill(16)
        temp_data = []

        for i in range(0, len(zfill_res), 4):
            temp_data.append(zfill_res[i : i + 4])

        result.append(" ".join(temp_data))

    return result
