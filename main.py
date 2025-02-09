from src.processing import filter_by_state, sort_by_date

default_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

if __name__ == "__main__":
    filter_state = filter_by_state(default_data, state="CANCELED")
    sorted_date = sort_by_date(default_data)

    print(filter_state)
    print(sorted_date)
