from abc import ABC, abstractmethod
from datetime import date


class Printable(ABC):
    @abstractmethod
    def print_info(self) -> None:
        """Вывести информацию об объекте."""
        raise NotImplementedError


class Book(Printable):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f'«{self.title}», {self.author}, {self.year} г.'

    def print_info(self):
        print(self.info())

    def __str__(self) -> str:
        return self.info()

    def __eq__(self, other):
        return isinstance(other, Book) and self.info() == other.info()

    @property
    def age(self):
        """Возраст книги в годах."""
        return date.today().year - self.year

    @classmethod
    def from_string(cls, book_data):
        """Создать книгу из строки: название, автор, год."""
        title, author, year = book_data.split(",")
        return cls(title.strip(), author.strip(), int(year))


class Ebook(Book):
    def __init__(self, title, author, year, format):
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        return f"{super().info()} Формат: {self.format}."


if __name__ == "__main__":
    book = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
    ebook = Ebook("Дюна", "Фрэнк Герберт", 1965, "EPUB")

    book.print_info()
    ebook.print_info()
    print(f"Возраст книги: {book.age} лет")
    print(f"Книги равны: {book == Book.from_string('Мастер и Маргарита, Михаил Булгаков, 1967')}")
