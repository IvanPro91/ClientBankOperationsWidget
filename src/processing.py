
def filter_by_state(list_data:list[dict], state:str="EXECUTED") -> list[dict]:
    """
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    :param list_data: Список словарей
    :param state: Значение для ключа
    :return:
    """
    r = [l for l in list_data if l['state'] == state]
    print(r)
    pass

def sort_by_date(list_data:list[dict], sort_reverse:bool=True):
    """
    Функция возвращает новый список, отсортированный по дате (date).
    :param list_data: Список словарей
    :param sort_reverse: Порядок сортировки
    :return: Возврат отсортированного листа со списком
    """
    pass