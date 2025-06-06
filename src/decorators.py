import os
from functools import wraps
from typing import Any


def log(filename: Any = None) -> Any:
    """
    Декоратор принимающий на вход необязательный аргумент filename
    :param filename: Имя файла для записи логов.
    :return: Возвращает функцию log_decorator.
    """

    def log_decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            write_log = ""
            try:
                write_log = f"{func.__name__} ok"
                func(*args, **kwargs)
            except Exception as err:
                write_log = f"{func.__name__} error {type(err).__name__} Inputs: {args} {kwargs}"
            finally:
                if not filename:
                    print(write_log)
                else:
                    with open(f"{path}/log/{filename}", mode="a") as f:
                        f.write(write_log + "\n")
                return func(*args, **kwargs)

        return wrapper

    return log_decorator
