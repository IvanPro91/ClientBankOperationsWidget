from datetime import datetime

from src.masks import account_card, get_mask_account


def mask_account_card(card_number: str) -> str:
    """
    Функция получения типа и номера карты или счета
    :param card_number: пример Visa Plantum XXXX, Счет XXXX
    :return: маска переданного номера
    """
    try:
        div_type_card = card_number.split()
        number = div_type_card[-1:][0]
        if len(number) == 20:
            mask_number = get_mask_account(number)
        elif len(number) == 16:
            mask_number = account_card(number)
        else:
            return "Неверный формат входного параметра"
        res = " ".join(div_type_card[:-1]) + " " + mask_number
        return res
    except Exception as err:
        return f"Error: {str(err)}"


def get_date(date: str) -> str:
    """
    Функция преобразования даты в нужный формат с помощью datetima
    :param date: строка например 2025-01-27T13:37:18.671407
    :return: ДД.ММ.ГГГГ
    """
    if len(date) == 0:
        return ""
    f_date = datetime.fromisoformat(date)
    return f_date.strftime("%d.%m.%Y")
