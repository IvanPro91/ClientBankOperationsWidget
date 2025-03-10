import os
from typing import Any
from unittest.mock import Mock, patch

import pytest

from src.finance import read_finance_csv_operation, read_finance_excel_operation

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@patch("csv.DictReader")
def test_read_finance_csv_operation(patch_csv: Any) -> None:
    """
    Тестирование функции read_finance_csv_operation
    :param patch_csv: Перехват csv.DictReader
    :return: None
    """
    data = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    patch_csv.return_value = data

    result = read_finance_csv_operation(ROOT_DIR + "/data/transactions.csv")
    assert result == data
    patch_csv.assert_called()


def test_error_read_finance_csv() -> None:
    """
    Тестирование на ошибку
    :return: None
    """
    with pytest.raises(ValueError):
        read_finance_csv_operation()


def test_read_finance_excel_operation() -> None:
    """
    Тестирование функции read_finance_excel_operation
    :return: None
    """

    mock_data_excel = Mock()
    data = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    mock_data_excel.to_dict.return_value = data
    mock_excel = Mock(return_value=mock_data_excel)
    with patch("pandas.read_excel", mock_excel):
        result = read_finance_excel_operation(ROOT_DIR + "/data/transactions_excel.xlsx")

    assert result == data


def test_error_read_finance_excel() -> None:
    """
    Тестирование на ошибку
    :return: None
    """
    with pytest.raises(ValueError):
        read_finance_excel_operation()
