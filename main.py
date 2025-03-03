from src.external_api import convert_currency
from src.utils import read_json_file

if __name__ == "__main__":
    list_data = read_json_file("data/operations.json")
    for data in list_data:
        sum_currency = convert_currency(data)
        print(sum_currency)
