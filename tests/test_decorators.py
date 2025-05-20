import pytest
from _pytest.capture import CaptureFixture

from src.decorators import log


def test_decorators() -> None:
    """
    Функция тестирования декоратора log с параметром
    :return: None
    """

    @log(filename="errors_log.txt")
    def num_div(x: int, y: int) -> float:
        return x / y

    decorator_1 = num_div(6, 2)
    assert decorator_1 == 3

    with pytest.raises(ZeroDivisionError):
        num_div(6, 0)


def test_capsys_decorators(capsys: CaptureFixture[str]) -> None:
    """
    Функция тестирования декоратора log без параметра
    :return: None
    """

    @log()
    def num_div(x: int, y: int) -> float:
        return x / y

    num_div(6, 2)
    read_out = capsys.readouterr()
    assert read_out.out == "num_div ok\n"

    with pytest.raises(ZeroDivisionError):
        num_div(6, 0)
