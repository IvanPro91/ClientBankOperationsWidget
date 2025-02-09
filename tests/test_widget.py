import pytest

from src.widget import get_date, mask_account_card

@pytest.mark.parametrize("data_number, result", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
])
def test_mask_account_card(data_number, result):
    assert mask_account_card(data_number) == result

@pytest.mark.parametrize("date, result", [
    ("2025-02-10T00:25:00.000000", "10.02.2025"),
    ("2024-02-09", "09.02.2024"),
    ("", ""),
])
def test_get_data(date, result):
    assert get_date(date) == result
    with pytest.raises(ValueError):
        assert get_date("2024-02-")