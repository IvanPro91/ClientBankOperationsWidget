import csv
from typing import Any

import pandas as pd


def read_finance_csv_operation(filename: str | None = None) -> list[dict[Any, Any]]:
    """
    Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями.
    :param filename: Путь к файлу CSV.
    :return: Список словарей с транзакциями.
    """
    if filename:
        with open(filename) as file:
            reader = csv.DictReader(file, delimiter=";")
            return list(reader)
    else:
        raise ValueError("filename не указан и равен None")


def read_finance_excel_operation(filename: str | None = None) -> list[dict[Any, Any]]:
    """
    Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями.
    :param filename: Путь к файлу Excel.
    :return: Список словарей с транзакциями.
    """
    if filename:
        excel_data = pd.read_excel(filename)
        group_data = excel_data.to_dict("records")
        return group_data
    else:
        raise ValueError("filename не указан и равен None")
