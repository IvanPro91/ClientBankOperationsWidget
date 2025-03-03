import json
from pathlib import Path

from src.utils import read_json_file


def test_read_json_file() -> None:
    """
    Тестирование конвертации файла json или его отсутствие
    :return: None
    """
    filename = str(Path().resolve()) + "/data/operations.json"
    test_no_file = read_json_file()
    test_file = read_json_file(filename)
    assert test_no_file == []
    assert test_file == json.load(open(filename, "r"))
