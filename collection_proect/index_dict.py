from typing import Dict, List, Any, Union
from collections import defaultdict


class IndexDict:
    """Пользовательская словарная коллекция для индексации книг"""

    def __init__(self):
        self._index_by_isbn: Dict[str, 'Book'] = {}
        self._index_by_author: Dict[str, List['Book']] = defaultdict(list)
        self._index_by_year: Dict[int, List['Book']] = defaultdict(list)
        self._index_by_genre: Dict[str, List['Book']] = defaultdict(list)

    def __getitem__(self, key: Any) -> Union['Book', List['Book']]:
        """Доступ к индексу по ключу"""
        if isinstance(key, str) and key in self._index_by_isbn:
            return self._index_by_isbn[key]
        elif isinstance(key, tuple):
            index_type, value = key
            if index_type == 'author':
                return self._index_by_author.get(value, [])
            elif index_type == 'year':
                return self._index_by_year.get(value, [])
            elif index_type == 'genre':
                return self._index_by_genre.get(value, [])
        raise KeyError(f"Ключ {key} не найден")

    def __setitem__(self, key: str, book: 'Book') -> None:
        """Добавление книги в индекс по ISBN"""
        self.add_book(book)

    def __delitem__(self, key: str) -> None:
        """Удаление книги из индекса по ISBN"""
        self.remove_book_by_isbn(key)

    def __len__(self) -> int:
        """Количество уникальных книг в индексе"""
        return len(self._index_by_isbn)

    def __iter__(self):
        """Итерация по ISBN"""
        return iter(self._index_by_isbn)

    def __repr__(self) -> str:
        """Строковое представление индекса"""
        return f"IndexDict({len(self)} книг, {len(self._index_by_author)} авторов)"

    def add_book(self, book: 'Book') -> None:
        """Добавление книги во все индексы"""
        self._index_by_isbn[book.isbn] = book
        self._index_by_author[book.author].append(book)
        self._index_by_year[book.year].append(book)
        self._index_by_genre[book.genre].append(book)

    def remove_book(self, book: 'Book') -> bool:
        """Удаление книги из всех индексов"""
        if book.isbn in self._index_by_isbn:
            del self._index_by_isbn[book.isbn]

            if book in self._index_by_author[book.author]:
                self._index_by_author[book.author].remove(book)
                if not self._index_by_author[book.author]:
                    del self._index_by_author[book.author]

            if book in self._index_by_year[book.year]:
                self._index_by_year[book.year].remove(book)
                if not self._index_by_year[book.year]:
                    del self._index_by_year[book.year]

            if book in self._index_by_genre[book.genre]:
                self._index_by_genre[book.genre].remove(book)
                if not self._index_by_genre[book.genre]:
                    del self._index_by_genre[book.genre]

            return True
        return False

    def remove_book_by_isbn(self, isbn: str) -> bool:
        """Удаление книги по ISBN"""
        if isbn in self._index_by_isbn:
            book = self._index_by_isbn[isbn]
            return self.remove_book(book)
        return False

    def search_by_author(self, author: str) -> List['Book']:
        """Поиск книг по автору"""
        return self._index_by_author.get(author, [])

    def search_by_year(self, year: int) -> List['Book']:
        """Поиск книг по году"""
        return self._index_by_year.get(year, [])

    def search_by_genre(self, genre: str) -> List['Book']:
        """Поиск книг по жанру"""
        return self._index_by_genre.get(genre, [])

    def search_by_isbn(self, isbn: str) -> 'Book':
        """Поиск книги по ISBN"""
        return self._index_by_isbn.get(isbn)

    def update_index(self, old_book: 'Book', new_book: 'Book') -> None:
        """Обновление индекса при изменении книги"""
        self.remove_book(old_book)
        self.add_book(new_book)