"""Шифр Цезаря для русского и английского алфавитов."""

# Алфавиты
RU_LOWER = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
RU_UPPER = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
EN_LOWER = "abcdefghijklmnopqrstuvwxyz"
EN_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def detect_language(text: str) -> str:
    """Определяет язык текста: 'ru' или 'en'.

    Считаем буквы каждого алфавита, возвращаем тот, где больше.
    """
    ru_count = 0
    en_count = 0

    for ch in text:
        if ch.lower() in RU_LOWER:
            ru_count += 1
        elif ch.lower() in EN_LOWER:
            en_count += 1

    if ru_count >= en_count:
        return "ru"
    return "en"


def shift_char(ch: str, k: int, alphabet_lower: str, alphabet_upper: str) -> str:
    """Сдвигает один символ на k позиций внутри алфавита.

    Если символ не буква — возвращает его без изменений.
    """
    # Строчная буква
    if ch in alphabet_lower:
        index = alphabet_lower.index(ch)
        new_index = (index + k) % len(alphabet_lower)
        return alphabet_lower[new_index]

    # Заглавная буква
    if ch in alphabet_upper:
        index = alphabet_upper.index(ch)
        new_index = (index + k) % len(alphabet_upper)
        return alphabet_upper[new_index]

    # Не буква — не трогаем
    return ch


def caesar(text: str, k: int, mode: str) -> str:
    """Шифрует или дешифрует текст шифром Цезаря.

    Args:
        text: исходный текст.
        k: сдвиг (целое число).
        mode: 'encrypt' или 'decrypt'.

    Returns:
        Преобразованный текст.
    """
    # Определяем язык
    lang = detect_language(text)

    if lang == "ru":
        lower = RU_LOWER
        upper = RU_UPPER
    else:
        lower = EN_LOWER
        upper = EN_UPPER

    # При дешифровании сдвигаем в обратную сторону
    if mode == "decrypt":
        k = -k

    result = ""
    for ch in text:
        result += shift_char(ch, k, lower, upper)

    return result


def main() -> None:
    """Интерактивный интерфейс шифра Цезаря."""
    print("Шифр Цезаря")
    print("Команды: encrypt / decrypt / exit")

    while True:
        command = input("\nКоманда: ").strip().lower()

        if command == "exit":
            print("Пока!")
            break

        if command not in ("encrypt", "decrypt"):
            print("Неизвестная команда. Попробуй encrypt, decrypt или exit.")
            continue

        text = input("Текст: ")
        k_str = input("Сдвиг (число): ")

        try:
            k = int(k_str)
        except ValueError:
            print("Сдвиг должен быть целым числом.")
            continue

        result = caesar(text, k, command)
        print("Результат:", result)


if __name__ == "__main__":
    main()