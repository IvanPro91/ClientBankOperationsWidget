import os

from src.finance import read_finance_csv_operation, read_finance_excel_operation
from src.find_word_regular import filter_by_word
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import read_json_file
from src.widget import get_date, mask_account_card

ROOT_DIR = os.path.dirname(__file__)

DIRECTORY_FILE = {
    1: f"{ROOT_DIR}/data/operations.json",
    2: f"{ROOT_DIR}/data/transactions.csv",
    3: f"{ROOT_DIR}/data/transactions_excel.xlsx",
}

func_answer = {
    1: "Получить информацию о транзакциях из JSON-файла",
    2: "Получить информацию о транзакциях из CSV-файла",
    3: "Получить информацию о транзакциях из XLSX-файла",
}

status = ["EXECUTED", "CANCELED", "PENDING"]
answer_yes_no = {"Да": True, "Нет": False}
sorted_min_max = {"по возрастанию": False, "по убыванию": True}


def get_user_menu() -> int:
    for answer in func_answer.keys():
        print(f"{answer}. {func_answer[answer]}")
    user_menu_input = input().strip()
    print(f"{func_answer[int(user_menu_input)]}")
    return int(user_menu_input)


def get_user_status() -> str:
    while True:
        print(f"Доступные для фильтровки статусы: {", ".join(status)}")
        input_data = input().strip()
        upper_filter_user = input_data.upper()

        if upper_filter_user not in status:
            print(f'Статус операции "{input_data}" недоступен.')
            print("Введите статус, по которому необходимо выполнить фильтрацию.")
        else:
            print(f'Операции отфильтрованы по статусу "{upper_filter_user}"')
            return upper_filter_user


def get_user_input_sorted() -> bool:
    input_data = input().strip()
    if input_data.title() in answer_yes_no.keys():
        return answer_yes_no[input_data.title()]
    return answer_yes_no["Да"]


def get_user_min_max_sorted() -> bool:
    input_data = input().strip()
    if input_data.lower() in sorted_min_max.keys():
        return sorted_min_max[input_data.lower()]
    return sorted_min_max["по возрастанию"]


def get_user_rub_transactions() -> bool:
    input_data = input().strip()
    if input_data.title() in answer_yes_no.keys():
        return answer_yes_no[input_data.title()]
    return answer_yes_no["Да"]


def get_user_filter_word() -> bool:
    input_data = input().strip()
    if input_data.title() in answer_yes_no.keys():
        return answer_yes_no[input_data.title()]
    return answer_yes_no["Да"]


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню ниже:")
    num_menu_input = get_user_menu()
    if num_menu_input == 1:
        data_read_file = read_json_file(DIRECTORY_FILE[num_menu_input])
    elif num_menu_input == 2:
        data_read_file = read_finance_csv_operation(DIRECTORY_FILE[num_menu_input])
    elif num_menu_input == 3:
        data_read_file = read_finance_excel_operation(DIRECTORY_FILE[num_menu_input])
    else:
        data_read_file = [{}]

    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    state = get_user_status()
    current_data = filter_by_state(data_read_file, state=state)

    print("Отсортировать операции по дате? Да/Нет")
    sort_date = get_user_input_sorted()
    if sort_date:
        print("Отсортировать по возрастанию или по убыванию?")
        sorted_min_max_value = get_user_min_max_sorted()
        current_data = sort_by_date(current_data, sort_reverse=sorted_min_max_value)

    print("Выводить только рублевые транзакции? Да/Нет")
    only_rub_transactions = get_user_rub_transactions()
    currency = "RUB" if only_rub_transactions else "USD"
    current_data = list(filter_by_currency(current_data, currency=currency))

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    filter_word = get_user_filter_word()
    if filter_word:
        find_word = input("Введите искомое слово\n").strip()
        current_data = filter_by_word(current_data, word=find_word)

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(current_data)}")

    for transaction in current_data:
        date = get_date(transaction["date"])
        amount = transaction["amount"] if "amount" in transaction else transaction["operationAmount"]["amount"]
        from_transaction = mask_account_card(transaction["from"])
        to_transaction = mask_account_card(transaction["to"])
        description = transaction["description"]
        currency_code = (
            transaction["currency_code"]
            if "currency_code" in transaction
            else transaction["operationAmount"]["currency"]["name"]
        )

        print(f"{date} {description}\n{from_transaction} -> {to_transaction}\nСумма: {amount} {currency_code}\n\n")


if __name__ == "__main__":
    main()
