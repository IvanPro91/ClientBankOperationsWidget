from src.widget import get_date, mask_account_card

default_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

if __name__ == "__main__":
    test_0 = mask_account_card("Visa Plantum 0123456789012345")
    test_1 = mask_account_card("Visa 2423423789542347")
    test_2 = mask_account_card("Счет 01234567896587412301")
    date = get_date("2025-01-27T13:37:18.671407")
    print(test_0)
    print(test_1)
    print(test_2)
    print(date)
