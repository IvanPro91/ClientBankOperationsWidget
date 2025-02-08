def account_card(card_number: str) -> str:
    """
    Функция преобразования номера карты в маску
    :param card_number: номер карты
    :return: маска
    """
    result = []
    starts_mask = "*" * (len(card_number) - 10)
    mask_card_number = f"{card_number[:6]}{starts_mask}{card_number[-4:]}"

    for i in range(0, len(mask_card_number), 4):
        result.append(mask_card_number[i : i + 4])

    return " ".join(result)


def get_mask_account(number_account: str) -> str:
    """
    Функция преобразования номера счета в нужный формат маскировки
    :param number_account: номер счета
    :return: маска
    """
    return f"**{number_account[len(number_account) - 4:]}"
