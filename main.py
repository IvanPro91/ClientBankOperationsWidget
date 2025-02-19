from src.decorators import log


# Реализация вызова функции с декоратором
@log(filename="errors_log.txt")
def num_div(x: int, y: int) -> float:
    return x / y


if __name__ == "__main__":
    num_div(6, 2)
    num_div(600, 22)
    num_div(2, 0)
