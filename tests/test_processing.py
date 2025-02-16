import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, result",
    [
        (
            "EXECUTED",
            [
                {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
                {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
            ],
        ),
        (
            "CANCELED",
            [
                {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
                {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
            ],
        ),
        ("", []),
    ],
)
def test_filter_by_state(
    filter_data_and_sorted: list[dict[str, str | int]], state: str, result: list[dict[str, str | int]]
) -> None:
    """
    Функция фильтра значений по ключу state
    :param filter_data_and_sorted: Тестовые данные
    :param state: Аргумент фильтра значения
    :param result: Результативные данные с параметризации
    :return: None
    """
    assert filter_by_state(filter_data_and_sorted, state=state) == result


def test_sort_by_date(filter_data_and_sorted: list[dict[str, str | int]]) -> None:
    """
    Функция сортировки данных по дате
    :param filter_data_and_sorted: Тестовые данные
    :return: None
    """
    assert sort_by_date(filter_data_and_sorted) == [
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    ]
    assert sort_by_date(filter_data_and_sorted, sort_reverse=False) == [
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
    ]
