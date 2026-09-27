"""Генератор паролей с настройками."""

import random
import string


# Наборы символов
LOWERCASE = string.ascii_lowercase          # abcdefghijklmnopqrstuvwxyz
UPPERCASE = string.ascii_uppercase          # ABCDEFGHIJKLMNOPQRSTUVWXYZ
DIGITS = string.digits                      # 0123456789
SPECIALS = "!@#$%^&*()-_=+[]{};:,.<>?/"


def build_charset(use_lower: bool, use_upper: bool,
                  use_digits: bool, use_specials: bool) -> str:
    """Собирает общий набор символов по настройкам."""
    charset = ""
    if use_lower:
        charset += LOWERCASE
    if use_upper:
        charset += UPPERCASE
    if use_digits:
        charset += DIGITS
    if use_specials:
        charset += SPECIALS
    return charset


def generate_password(length: int, charset: str) -> str:
    """Генерирует пароль заданной длины из набора символов."""
    password = ""
    for _ in range(length):
        password += random.choice(charset)
    return password


def print_header() -> None:
    """Печатает шапку программы."""
    print()
    print("=" * 40)
    print("       ГЕНЕРАТОР ПАРОЛЕЙ")
    print("=" * 40)


def print_menu(settings: dict) -> None:
    """Печатает текущие настройки."""
    print()
    print("Текущие настройки:")
    print(f"  1. Длина пароля:        {settings['length']}")

    mark_lower = "[+]" if settings["lower"] else "[ ]"
    mark_upper = "[+]" if settings["upper"] else "[ ]"
    mark_digits = "[+]" if settings["digits"] else "[ ]"
    mark_specials = "[+]" if settings["specials"] else "[ ]"

    print(f"  2. Строчные буквы:      {mark_lower}")
    print(f"  3. Заглавные буквы:     {mark_upper}")
    print(f"  4. Цифры:               {mark_digits}")
    print(f"  5. Спецсимволы:         {mark_specials}")
    print()
    print("  g — сгенерировать пароль")
    print("  q — выход")
    print()


def ask_int(prompt: str, min_value: int = 1, max_value: int = 128) -> int:
    """Спрашивает целое число в заданных границах."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("  Введите целое число.")
            continue
        if value < min_value or value > max_value:
            print(f"  Число должно быть от {min_value} до {max_value}.")
            continue
        return value


def toggle(current: bool) -> bool:
    """Переключает флаг True/False."""
    return not current


def main() -> None:
    """Главный цикл программы."""
    # Настройки по умолчанию
    settings = {
        "length": 12,
        "lower": True,
        "upper": True,
        "digits": True,
        "specials": False,
    }

    print_header()

    while True:
        print_menu(settings)
        command = input("Выберите пункт: ").strip().lower()

        if command == "q":
            print("\nПока!")
            break

        elif command == "1":
            settings["length"] = ask_int(
                "  Новая длина пароля (4-128): ", 4, 128
            )

        elif command == "2":
            settings["lower"] = toggle(settings["lower"])

        elif command == "3":
            settings["upper"] = toggle(settings["upper"])

        elif command == "4":
            settings["digits"] = toggle(settings["digits"])

        elif command == "5":
            settings["specials"] = toggle(settings["specials"])

        elif command == "g":
            charset = build_charset(
                settings["lower"],
                settings["upper"],
                settings["digits"],
                settings["specials"],
            )

            if charset == "":
                print("\n  [!] Не выбран ни один набор символов!")
                print("  Включите хотя бы один пункт (2-5).")
                continue

            password = generate_password(settings["length"], charset)
            print()
            print("  " + "-" * 36)
            print(f"  Ваш пароль: {password}")
            print("  " + "-" * 36)

        else:
            print("  Неизвестная команда.")


if __name__ == "__main__":
    main()