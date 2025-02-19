import pytest

from src.masks import account_card, get_mask_account


def test_get_mask_card_number() -> None:
    """
    Функция тестирования масок карт
    :return: None
    """
    assert account_card("21541221421212525845") == "2154 12** **** **** 5845"
    with pytest.raises(ValueError):
        account_card("215412214212125")

    with pytest.raises(ValueError):
        account_card("")


def test_get_mask_account() -> None:
    """
    Функция тестирования номеров счета
    :return: None
    """
    assert get_mask_account("9866548755412145") == "**2145"
    with pytest.raises(ValueError):
        get_mask_account("1154122")

    with pytest.raises(ValueError):
        get_mask_account("")
