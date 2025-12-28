from typing import Iterator, Union, List, Any


class BookCollection:
    """Пользовательская списковая коллекция для хранения книг"""

    def __init__(self, books: List['Book'] = None):
        self._books = books if books is not None else []

    def __getitem__(self, key: Union[int, slice]) -> Union['Book', 'BookCollection']:
        """Доступ по индексу или срезу"""
        if isinstance(key, slice):
            return BookCollection(self._books[key])
        return self._books[key]

    def __iter__(self) -> Iterator['Book']:
        """Итерация по коллекции"""
        return iter(self._books)

    def __len__(self) -> int:
        """Количество книг в коллекции"""
        return len(self._books)

    def __repr__(self) -> str:
        """Строковое представление коллекции"""
        return f"BookCollection({len(self)} книг)"

    def add(self, book: 'Book') -> None:
        """Добавление книги в коллекцию"""
        if book not in self._books:
            self._books.append(book)

    def remove(self, book: 'Book') -> bool:
        """Удаление книги из коллекции"""
        if book in self._books:
            self._books.remove(book)
            return True
        return False

    def remove_by_index(self, index: int) -> 'Book':
        """Удаление книги по индексу"""
        if 0 <= index < len(self._books):
            return self._books.pop(index)
        raise IndexError("Индекс вне диапазона")

    def clear(self) -> None:
        """Очистка коллекции"""
        self._books.clear()

    def get_books(self) -> List['Book']:
        """Получение списка всех книг"""
        return self._books.copy()