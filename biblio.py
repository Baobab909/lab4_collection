import random
from typing import Optional
from models.book import Book
from models.library import Library


class LibrarySimulation:
    """Класс для псевдослучайной симуляции работы библиотеки"""

    def __init__(self, library: Library):
        self.library = library
        self.events_log = []

        # Список возможных событий с их вероятностями
        self.events = [
            (self.event_add_book, 0.2),
            (self.event_remove_random_book, 0.15),
            (self.event_search_by_author, 0.15),
            (self.event_search_by_genre, 0.15),
            (self.event_search_by_year, 0.1),
            (self.event_update_random_book, 0.1),
            (self.event_search_nonexistent_book, 0.05),
        ]

    def log_event(self, message: str) -> None:
        """Логирование события"""
        self.events_log.append(message)
        print(message)

    def event_add_book(self) -> None:
        """Событие: добавление новой книги"""
        # Генерация случайной книги
        titles = ["Война и мир", "Преступление и наказание", "1984",
                  "Мастер и Маргарита", "Гарри Поттер", "Властелин колец"]
        authors = ["Лев Толстой", "Фёдор Достоевский", "Джордж Оруэлл",
                   "Михаил Булгаков", "Джоан Роулинг", "Джон Толкин"]
        genres = ["Роман", "Фантастика", "Детектив", "Фэнтези", "Научная литература"]

        title = random.choice(titles) + f" {random.randint(1, 100)}"
        author = random.choice(authors)
        year = random.randint(1900, 2023)
        genre = random.choice(genres)
        isbn = f"978-{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"

        book = Book(title, author, year, genre, isbn)

        if self.library.add_book(book):
            self.log_event(f"Добавлена новая книга: {book.title} (ISBN: {isbn})")
        else:
            self.log_event(f"Книга с ISBN {isbn} уже существует")

    def event_remove_random_book(self) -> None:
        """Событие: удаление случайной книги"""
        if len(self.library.book_collection) == 0:
            self.log_event("Нет книг для удаления")
            return

        # Выбор случайной книги
        random_index = random.randint(0, len(self.library.book_collection) - 1)
        book = self.library.book_collection[random_index]

        if self.library.remove_book(book):
            self.log_event(f"Удалена книга: {book.title} (ISBN: {book.isbn})")
        else:
            self.log_event(f"Не удалось удалить книгу {book.title}")

    def event_search_by_author(self) -> None:
        """Событие: поиск по автору"""
        authors = list(self.library.index_dict._index_by_author.keys())
        if not authors:
            self.log_event("Нет авторов в библиотеке")
            return

        author = random.choice(authors)
        books = self.library.find_by_author(author)

        self.log_event(f"Поиск по автору '{author}': найдено {len(books)} книг")
        for i, book in enumerate(books[:3], 1):  # Показываем только первые 3
            self.log_event(f"    {i}. {book.title} ({book.year})")

    def event_search_by_genre(self) -> None:
        """Событие: поиск по жанру"""
        genres = list(self.library.index_dict._index_by_genre.keys())
        if not genres:
            self.log_event("Нет книг по жанрам")
            return

        genre = random.choice(genres)
        books = self.library.find_by_genre(genre)

        self.log_event(f"Поиск по жанру '{genre}': найдено {len(books)} книг")
        for i, book in enumerate(books[:3], 1):
            self.log_event(f"    {i}. {book.title} - {book.author}")

    def event_search_by_year(self) -> None:
        """Событие: поиск по году"""
        years = list(self.library.index_dict._index_by_year.keys())
        if not years:
            self.log_event("Нет книг по годам")
            return

        year = random.choice(years)
        books = self.library.find_by_year(year)

        self.log_event(f"Поиск по году {year}: найдено {len(books)} книг")
        for i, book in enumerate(books[:2], 1):
            self.log_event(f"    {i}. {book.title} - {book.author}")

    def event_update_random_book(self) -> None:
        """Событие: обновление случайной книги"""
        if len(self.library.book_collection) == 0:
            self.log_event("Нет книг для обновления")
            return
        random_index = random.randint(0, len(self.library.book_collection) - 1)
        old_book = self.library.book_collection[random_index]
        new_book = Book(
            title=old_book.title + " (обновленное издание)",
            author=old_book.author,
            year=old_book.year + 1,
            genre=old_book.genre,
            isbn=f"NEW-{old_book.isbn}"
        )

        if self.library.update_book(old_book.isbn, new_book):
            self.log_event(f"Обновлена книга: {old_book.title} -> {new_book.title}")
        else:
            self.log_event(f"Не удалось обновить книгу {old_book.title}")

    def event_search_nonexistent_book(self) -> None:
        """Событие: поиск несуществующей книги"""
        fake_isbn = f"FAKE-{random.randint(1000, 9999)}"
        book = self.library.find_by_isbn(fake_isbn)

        if book is None:
            self.log_event(f"Поиск несуществующей книги (ISBN: {fake_isbn}): не найдено")
        else:
            self.log_event(f"Найдена книга, которой не должно быть: {book.title}")

    def run_simulation(self, steps: int = 20, seed: Optional[int] = None) -> None:
        """Основная функция симуляции"""
        if seed is not None:
            random.seed(seed)
            self.log_event(f"Установлен seed: {seed}")
        self.log_event(f"Начало симуляции ({steps} шагов)")

        for step in range(1, steps + 1):
            self.log_event(f"\nШаг {step}:")
            events, weights = zip(*self.events)
            chosen_event = random.choices(events, weights=weights, k=1)[0]
            chosen_event()
        self.log_event(f"    Всего событий: {len(self.events_log)}")
        self.log_event(f"    Книг в библиотеке: {len(self.library.book_collection)}")

    def get_log(self) -> list:
        """Получение лога событий"""
        return self.events_log