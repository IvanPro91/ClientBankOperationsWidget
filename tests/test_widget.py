import pytest

from src.widget import get_date, mask_account_card

@pytest.mark.parametrize("data_number, result", [
    ("Visa Platinum 70007922548789606361", "Visa Platinum 7000 79** **** **** 6361"),
    ("Счет 7365410843014305", "Счет **4305"),
    ("MasterCard 71583007548734726758", "MasterCard 7158 30** **** **** 6758"),
])
def test_mask_account_card(data_number, result):
    assert mask_account_card(data_number) == result

@pytest.mark.parametrize("date, result", [
    ("2025-02-10T00:25:00.000000", "10.02.2025"),
    ("2024-02-09", "09.02.2024"),
])
def test_get_data(date, result):
    assert get_date(date) == result
    with pytest.raises(ValueError):
        assert get_date("2024-02-")
        assert get_date("")