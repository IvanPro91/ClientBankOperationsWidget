from typing import Any
from unittest.mock import Mock, patch

import pytest
import requests

from src.external_api import convert_currency


@patch("requests.get")
def test_patch_convert_currency(mock_get: Any, test_data_mock_requests: dict) -> None:
    """
    Тестирование Patch конвертация валюты
    :param mock_get: Объект результата захвата requests
    :param test_data_mock_requests: Фикстура с данными requests
    :return: None
    """

    data = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1562198399, "rate": 63.315897},
        "date": "2019-07-03",
        "historical": True,
        "result": 520543.416119,
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = data
    result = convert_currency(test_data_mock_requests)
    assert result == 520543.416119
    mock_get.assert_called()


def test_raise_convert_currency() -> None:
    """
    Фукнция тестирования на ошибку
    :return: None
    """
    with pytest.raises(ValueError):
        convert_currency({})


def test_rub_convert_currency() -> None:
    """
    Фукнция тестирования на code RUB
    :return: None
    """
    data = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    result = convert_currency(data)
    assert result == 31957.58


def test_mock_convert_currency(test_data_mock_requests: dict) -> None:
    """
    Тестирование Mock конвертация валюты
    :param test_data_mock_requests: Фикстура с данными requests
    :return: None
    """
    mock_response = Mock()
    data = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1562198399, "rate": 63.315897},
        "date": "2019-07-03",
        "historical": True,
        "result": 520543.416119,
    }
    mock_response.status_code = 200
    mock_response.json.return_value = data

    mock_get = Mock(return_value=mock_response)
    requests.get = mock_get

    result = convert_currency(test_data_mock_requests)
    assert result == 520543.416119
    requests.get = requests.get
