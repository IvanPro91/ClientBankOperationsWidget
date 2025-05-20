import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, result",
    [
        ("USD", [939719570, 142264268, 895315941]),
        ("RUB", [873106923, 594226727]),
    ],
)
def test_filter_by_currency(transactions: list[dict], currency: str, result: list[int]) -> None:
    """
    Функция тестирования currency code
    :param transactions: Тестовые данные
    :param currency: Значение currency code параметризации
    :param result: Значение возврата параметризации
    :return: None
    """
    data_list = list(filter_by_currency(transactions, currency))
    list_ids = [int(ids["id"]) for ids in data_list]

    assert list_ids == result

    with pytest.raises(ValueError):
        filter_by_currency([], currency=currency)

    with pytest.raises(ValueError):
        filter_by_currency(transactions, currency="")


def test_transaction_descriptions(transactions: list[dict]) -> None:
    """
    Функция тестирования описания транзакций
    :param transactions: Тестовые данные
    :return: None
    """
    data = transaction_descriptions(transactions)
    error_transaction = transaction_descriptions([])

    assert next(data) == "Перевод организации"
    assert next(data) == "Перевод со счета на счет"
    assert next(data) == "Перевод со счета на счет"
    assert next(data) == "Перевод с карты на карту"
    assert next(data) == "Перевод организации"

    with pytest.raises(ValueError):
        next(error_transaction)


@pytest.mark.parametrize(
    "start, stop, result",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (1001, 1003, ["0000 0000 0000 1001", "0000 0000 0000 1002"]),
        (9991, 9993, ["0000 0000 0000 9991", "0000 0000 0000 9992"]),
    ],
)
def test_card_number_generator(start: int, stop: int, result: list[str]) -> None:
    """
    Функция тестирования генерации номеров карт
    :param start: Стартовое значение параметризации
    :param stop: Конечное значение параметризации
    :param result: Значение результата с параметризации
    :return: None
    """
    assert card_number_generator(start, stop) == result
    with pytest.raises(ValueError):
        card_number_generator(0, 0)
