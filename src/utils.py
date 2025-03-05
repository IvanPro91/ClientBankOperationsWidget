import json
import logging
import os
import traceback

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

utils_logger = logging.getLogger(__name__)
utils_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(ROOT_DIR + "/log/stream_logger.log")
file_formatter = logging.Formatter("%(asctime)s %(module)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)


def read_json_file(filename: str = "") -> list:
    """
    Функция чтения JSON-файла
    :param filename: Путь к файлу JSON
    :return: Список словарей с данными о финансовых транзакциях.
    """
    try:
        data_json = json.load(open(filename, "r"))
        utils_logger.info("read_json_file -> file read success")
        return list(data_json)
    except Exception:
        utils_logger.error(f"read_json_file -> {traceback.format_exc()}")
        return []
