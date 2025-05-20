def filter_by_state(list_data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    :param list_data: Список словарей
    :param state: Значение для ключа
    :return: Список словарей отсортированные по ключу
    """
    return [dict_data_state for dict_data_state in list_data if dict_data_state.get("state", "") == state]


def sort_by_date(list_data: list[dict], sort_reverse: bool = True) -> list[dict]:
    """
    Функция возвращает новый список, отсортированный по дате (date).
    :param list_data: Список словарей
    :param sort_reverse: Порядок сортировки
    :return: Возврат отсортированного листа со списком
    """
    return sorted(list_data, key=lambda x: x["date"], reverse=sort_reverse)
