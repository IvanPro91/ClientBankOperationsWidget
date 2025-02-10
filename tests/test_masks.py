import pytest

from src.masks import get_mask_account, account_card

def test_get_mask_card_number():
    assert account_card("21541221421212525845") == "2154 12** **** **** 5845"
    with pytest.raises(Exception):
        account_card("215412214212125")
        account_card("")

def test_get_mask_account():
    assert get_mask_account("9866548755412145") == "**2145"
    with pytest.raises(Exception):
        get_mask_account("1154122")
        get_mask_account("")