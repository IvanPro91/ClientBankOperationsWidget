import pytest

from src.masks import get_mask_account, account_card

@pytest.mark.parametrize("number, result", [
    ("21541221421212525845", "2154 12** **** **** 5845"),
    ("215412214212125", "2154 12** ***2 125"),
    ("", ""),
])
def test_get_mask_card_number(number, result):
    assert account_card(number) == result

def test_get_mask_account(account_number):
    assert get_mask_account(account_number) == "**4511"