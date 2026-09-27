def print_pack_report(n: int) -> None:
    """Печатает отчёт о фасовке пирожных от n до 1.

    Args:
        n: целое положительное число больше 1.
    """
    for x in range(n, 0, -1):
        if x % 3 == 0 and x % 5 == 0:
            print(x, "- расфасуем по 3 или по 5")
        elif x % 5 == 0:
            print(x, "- расфасуем по 5")
        elif x % 3 == 0:
            print(x, "- расфасуем по 3")
        else:
            print(x, "- не заказываем!")


print_pack_report(15)