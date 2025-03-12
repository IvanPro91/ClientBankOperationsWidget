from src.find_word_regular import count_all_by_category, filter_by_word


def test_filter_by_word(transactions: list[dict], current_re_filter: list[dict]) -> None:
    assert filter_by_word(transactions, "карту") == current_re_filter


def test_count_all_by_category(transactions: list[dict]) -> None:
    assert count_all_by_category(transactions, ["Перевод организации"]) == {"Перевод организации": 2}
    assert count_all_by_category(transactions, ["Перевод с карты на карту"]) == {"Перевод с карты на карту": 1}
