"""Модуль калькулятора с базовыми арифметическими операциями."""


def add_numbers(a: float, b: float) -> float:
    """Складывает два числа.

    Args:
        a: первое число.
        b: второе число.

    Returns:
        Сумма a и b.
    """
    return a + b


def subtract_numbers(a: float, b: float) -> float:
    """Вычитает b из a.

    Args:
        a: уменьшаемое.
        b: вычитаемое.

    Returns:
        Разность a и b.
    """
    return a - b


def multiply_numbers(a: float, b: float) -> float:
    """Умножает два числа.

    Args:
        a: первый множитель.
        b: второй множитель.

    Returns:
        Произведение a и b.
    """
    return a * b


def divide_numbers(a: float, b: float) -> float:
    """Делит a на b.

    Args:
        a: делимое.
        b: делитель.

    Returns:
        Частное a и b.

    Raises:
        ZeroDivisionError: если b равно нулю.
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b


def main() -> None:
    """Запускает интерактивный калькулятор."""
    while True:
        expr = input(">>> ")

        if expr == "exit":
            break

        parts = expr.split()

        if len(parts) != 3:
            print("Формат: число операция число (например: 2 + 3)")
            continue

        a = float(parts[0])
        op = parts[1]
        b = float(parts[2])

        if op == "+":
            print(add_numbers(a, b))
        elif op == "-":
            print(subtract_numbers(a, b))
        elif op == "*":
            print(multiply_numbers(a, b))
        elif op == "/":
            try:
                print(divide_numbers(a, b))
            except ZeroDivisionError as e:
                print("Ошибка:", e)
        else:
            print("Неизвестная операция:", op)


if __name__ == "__main__":
    main()