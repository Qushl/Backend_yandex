import random

# Картинки виселицы — 7 штук
HANGMAN_PICS = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]


# Список слов для игры
WORDS = [
    "питон", "алгоритм", "компьютер", "функция", "переменная",
    "цикл", "массив", "константа", "компилятор", "библиотека",
    "модуль", "класс", "объект", "рекурсия", "итерация",
    "условие", "оператор", "строка", "список", "словарь",

    "медведь", "лиса", "волк", "заяц", "белка", "ёжик",
    "тигр", "лев", "слон", "жираф", "пингвин", "дельфин",

    "шоколад", "печенье", "мороженое", "пирожное", "торт",
    "яблоко", "груша", "малина", "клубника", "картофель",

    "дерево", "солнце", "звезда", "облако", "ветер",
    "машина", "корабль", "велосипед", "учитель", "художник",
    "библиотека", "университет", "путешествие", "приключение",
]


def pick_word() -> str:
    """Выбирает случайное слово из списка."""
    return random.choice(WORDS)


def show_state(word: str, guessed: set, wrong: int) -> None:
    """Показывает виселицу, угаданные буквы и ошибки.

    Args:
        word: загаданное слово.
        guessed: множество угаданных букв.
        wrong: количество ошибок.
    """
    print(HANGMAN_PICS[wrong])

    # Открытая часть слова
    display = ""
    for ch in word:
        if ch in guessed:
            display += ch + " "
        else:
            display += "_ "
    print("Слово:", display)
    print("Ошибок:", wrong, "из", len(HANGMAN_PICS) - 1)
    print("Угаданные буквы:", " ".join(sorted(guessed)) if guessed else "—")
    print()


def ask_letter(guessed: set) -> str:
    """Спрашивает букву у игрока. Возвращает одну букву."""
    while True:
        raw = input("Введите букву: ").strip().lower()

        if len(raw) != 1:
            print("  Нужна ровно одна буква.")
            continue

        if not raw.isalpha():
            print("  Это не буква.")
            continue

        if raw in guessed:
            print("  Эту букву вы уже называли.")
            continue

        return raw


def play_round() -> None:
    """Один раунд игры."""
    word = pick_word()
    guessed = set()
    wrong = 0
    max_wrong = len(HANGMAN_PICS) - 1

    print("=" * 40)
    print("       ВИСЕЛИЦА")
    print("=" * 40)
    print(f"Загадано слово из {len(word)} букв.")
    print()

    while True:
        show_state(word, guessed, wrong)

        # Проверка победы: все буквы слова угаданы
        won = True
        for ch in word:
            if ch not in guessed:
                won = False
                break
        if won:
            print("🎉 Победа! Вы угадали слово:", word)
            return

        # Проверка проигрыша
        if wrong >= max_wrong:
            print("💀 Вы проиграли. Было загадано слово:", word)
            return

        letter = ask_letter(guessed)
        guessed.add(letter)

        if letter in word:
            print("  ✅ Есть такая буква!")
        else:
            print("  ❌ Нет такой буквы.")
            wrong += 1
        print()


def main() -> None:
    """Главный цикл игры."""
    while True:
        play_round()

        print()
        again = input("Сыграть ещё раз? (y/n): ").strip().lower()
        if again != "y":
            print("Конец игры!")
            break
        print()


if __name__ == "__main__":
    main()