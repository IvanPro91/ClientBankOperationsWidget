import json
import os

from src.utils import read_json_file

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_read_json_file() -> None:
    """
    Тестирование конвертации файла json или его отсутствие
    :return: None
    """
    filename = ROOT_DIR + "/data/operations.json"
    test_no_file = read_json_file()
    test_file = read_json_file(filename)
    assert test_no_file == []
    assert test_file == json.load(open(filename, "r"))
