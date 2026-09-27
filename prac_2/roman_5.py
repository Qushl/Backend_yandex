"""Конвертер между арабскими и римскими числами."""


ROMAN_MAP = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def int_to_roman(n: int) -> str:
    """Переводит арабское число в римскую запись."""
    if n < 1 or n > 3999:
        raise ValueError("Число должно быть от 1 до 3999")

    result = ""
    for value, symbol in ROMAN_MAP:
        while n >= value:
            result += symbol
            n -= value
    return result


def roman_to_int(roman: str) -> int:
    """Переводит римскую запись в арабское число."""
    roman = roman.upper().strip()

    values = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000,
    }

    for ch in roman:
        if ch not in values:
            raise ValueError(f"Неизвестный символ: {ch}")

    total = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman) and values[roman[i]] < values[roman[i + 1]]:
            total += values[roman[i + 1]] - values[roman[i]]
            i += 2
        else:
            total += values[roman[i]]
            i += 1
    return total


def print_header() -> None:
    """Печатает шапку."""
    print()
    print("=" * 40)
    print("        РИМСКИЙ КОНВЕРТЕР")
    print("=" * 40)


def print_menu() -> None:
    """Печатает меню."""
    print()
    print("Выберите что хотите сделать")
    print("  1 — число → римское   (например: 42 → XLII)")
    print("  2 — римское → число   (например: XLII → 42)")
    print("  3 — проверка обратимости")
    print("  q — выход")
    print()


def mode_int_to_roman() -> None:
    """Режим 1: число → римское."""
    raw = input("Введите число (1-3999): ").strip()
    try:
        n = int(raw)
    except ValueError:
        print("  Это не целое число.")
        return

    try:
        print(f"  {n} → {int_to_roman(n)}")
    except ValueError as e:
        print(f"  Ошибка: {e}")


def mode_roman_to_int() -> None:
    """Режим 2: римское → число."""
    raw = input("Введите римское число: ").strip()
    if raw == "":
        print("  Пустой ввод.")
        return

    try:
        print(f"  {raw.upper()} → {roman_to_int(raw)}")
    except ValueError as e:
        print(f"  Ошибка: {e}")


def mode_round_trip() -> None:
    """Режим 3: проверка обратимости."""
    raw = input("Введите число (1-3999): ").strip()
    try:
        n = int(raw)
    except ValueError:
        print("  Это не целое число.")
        return

    try:
        roman = int_to_roman(n)
        back = roman_to_int(roman)
    except ValueError as e:
        print(f"  Ошибка: {e}")
        return

    status = "OK" if back == n else "ОШИБКА"
    print(f"  {n} → {roman} → {back}   [{status}]")


def main() -> None:
    """Главный цикл программы."""
    print_header()

    while True:
        print_menu()
        command = input("Ваш выбор: ").strip().lower()

        if command == "q":
            print("\nКонец программы!")
            break
        elif command == "1":
            mode_int_to_roman()
        elif command == "2":
            mode_roman_to_int()
        elif command == "3":
            mode_round_trip()
        else:
            print("  Неизвестная команда. Введите 1, 2, 3 или q.")


if __name__ == "__main__":
    main()