from src.decorators import log


# Реализация вызова функции с декоратором
@log(filename="error_log.txt")
def num_div(x: int, y: int) -> float:
    return x / y


if __name__ == "__main__":
    num_div(2, 0)
