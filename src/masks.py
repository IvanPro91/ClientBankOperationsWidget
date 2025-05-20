import logging
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

masks_logger = logging.getLogger(__name__)
masks_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(ROOT_DIR + "/log/stream_logger.log")
file_formatter = logging.Formatter("%(asctime)s %(module)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)


def account_card(card_number: str) -> str:
    """
    Функция преобразования номера карты в маску
    :param card_number: номер карты
    :return: маска
    """
    len_number = len(card_number)
    if len_number != 16:
        masks_logger.error(f"Invalid length card number: len = {len_number} waiting for 16")
        raise ValueError(f"Invalid length card number: len = {len_number} waiting for 16")

    result = []
    starts_mask = "*" * (len(card_number) - 10)
    mask_card_number = f"{card_number[:6]}{starts_mask}{card_number[-4:]}"

    for i in range(0, len(mask_card_number), 4):
        result.append(mask_card_number[i : i + 4])

    masks_logger.info("account_card -> success")
    return " ".join(result)


def get_mask_account(number_account: str) -> str:
    """
    Функция преобразования номера счета в нужный формат маскировки
    :param number_account: номер счета
    :return: маска
    """
    len_number = len(number_account)
    if len_number != 20:
        masks_logger.error(f"Invalid length card number: len = {len_number} waiting for 20")
        raise ValueError(f"Invalid length card number: len = {len_number} waiting for 20")

    masks_logger.info("get_mask_account -> success")
    return f"**{number_account[len(number_account) - 4:]}"
