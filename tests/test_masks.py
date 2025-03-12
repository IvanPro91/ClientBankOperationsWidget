import pytest

from src.masks import account_card, get_mask_account


def test_get_mask_card_number() -> None:
    """
    Функция тестирования масок карт
    :return: None
    """
    assert account_card("2154122142121252") == "2154 12** **** 1252"
    with pytest.raises(ValueError):
        account_card("21541221421212")

    with pytest.raises(ValueError):
        account_card("")


def test_get_mask_account() -> None:
    """
    Функция тестирования номеров счета
    :return: None
    """
    assert get_mask_account("98665487554121452312") == "**2312"
    with pytest.raises(ValueError):
        get_mask_account("1154122")

    with pytest.raises(ValueError):
        get_mask_account("")
