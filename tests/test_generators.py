import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "currency, result",
    [
        ("USD", [939719570, 142264268, 895315941]),
        ("RUB", [873106923, 594226727]),
    ],
)
def test_filter_by_currency(transactions, currency, result):
    data_list = list(filter_by_currency(transactions, currency))
    list_ids = [int(ids["id"]) for ids in data_list]

    assert list_ids == result

    with pytest.raises(ValueError):
        assert filter_by_currency([], currency=currency)

    with pytest.raises(ValueError):
        assert filter_by_currency([], currency="")


def test_transaction_descriptions(transactions):
    assert list(transaction_descriptions(transactions)) == ['Перевод организации', 'Перевод со счета на счет',
                                                            'Перевод со счета на счет', 'Перевод с карты на карту',
                                                            'Перевод организации']
    with pytest.raises(ValueError):
        assert transaction_descriptions([])


@pytest.mark.parametrize(
    "start, stop, result",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (1001, 1003, ["0000 0000 0000 1001", "0000 0000 0000 1002"]),
        (9991, 9993, ["0000 0000 0000 9991", "0000 0000 0000 9992"]),
    ],
)
def test_card_number_generator(start, stop, result):
    assert card_number_generator(start, stop) == result
    with pytest.raises(ValueError):
        assert card_number_generator(0, 0)
