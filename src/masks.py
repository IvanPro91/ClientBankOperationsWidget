def account_card(card_number: str) -> str:
    """
    Функция преобразования номера карты в маску
    :param card_number: номер карты
    :return: маска
    """
    len_number = len(card_number)
    if len_number != 20:
        raise Exception(f"Invalid length card number: len = {len_number} waiting for 20")

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
    len_number = len(number_account)
    if len_number != 16:
        raise Exception(f"Invalid length card number: len = {len_number} waiting for 16")
    return f"**{number_account[len(number_account) - 4:]}"
