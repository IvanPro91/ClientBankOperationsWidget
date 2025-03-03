import os
from datetime import datetime

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной API_KEY из .env-файла
API_KEY = os.getenv("API_KEY")


def convert_currency(dict_data: dict) -> float:
    """
    Функция конвертации валюты из USD и EUR в рубли.
    :param dict_data: Принимает на вход словарь с данными о транзакции.
    :return: Возвращает сумму транзакции (ключ amount) в рублях, тип данных float
    """
    try:
        currency_code = dict_data["operationAmount"]["currency"]["code"]
        if currency_code != "RUB":
            amount = float(dict_data["operationAmount"]["amount"])
            convert_to = "RUB"
            date_transaction = datetime.fromisoformat(dict_data["date"])
            convert_from = currency_code

            url = "https://api.apilayer.com/exchangerates_data/convert"
            params = {
                "to": convert_to,
                "from": convert_from,
                "amount": amount,
                "date": date_transaction.strftime("%Y-%m-%d"),
            }
            headers = {"apikey": API_KEY}

            response = requests.get(url, params=params, headers=headers)
            if response.status_code == 200:
                response_data = response.json()
                return float(response_data["result"])
        return float(dict_data["operationAmount"]["amount"])
    except Exception:
        raise ValueError("Not find key[s] (operationAmount, currency, code)")
