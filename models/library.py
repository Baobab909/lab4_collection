from collection_proect.book_collection import BookCollection
from collection_proect.index_dict import IndexDict


class Library:
    """Класс библиотеки, управляющий коллекциями книг и индексами"""

    def __init__(self, name: str):
        self.name = name
        self.book_collection = BookCollection()
        self.index_dict = IndexDict()

    def __repr__(self) -> str:
        """Строковое представление библиотеки"""
        return f"Library('{self.name}', книг: {len(self.book_collection)})"

    def add_book(self, book: 'Book') -> bool:
        """Добавление книги в библиотеку"""
        if book not in self.book_collection:
            self.book_collection.add(book)
            self.index_dict.add_book(book)
            return True
        return False

    def remove_book(self, book: 'Book') -> bool:
        """Удаление книги из библиотеки"""
        if self.book_collection.remove(book):
            self.index_dict.remove_book(book)
            return True
        return False

    def remove_book_by_isbn(self, isbn: str) -> bool:
        """Удаление книги по ISBN"""
        book = self.index_dict.search_by_isbn(isbn)
        if book:
            return self.remove_book(book)
        return False

    def find_by_author(self, author: str) -> BookCollection:
        """Поиск книг по автору"""
        books = self.index_dict.search_by_author(author)
        return BookCollection(books)

    def find_by_year(self, year: int) -> BookCollection:
        """Поиск книг по году"""
        books = self.index_dict.search_by_year(year)
        return BookCollection(books)

    def find_by_genre(self, genre: str) -> BookCollection:
        """Поиск книг по жанру"""
        books = self.index_dict.search_by_genre(genre)
        return BookCollection(books)

    def find_by_isbn(self, isbn: str) -> 'Book':
        """Поиск книги по ISBN"""
        return self.index_dict.search_by_isbn(isbn)

    def find_by_title(self, title_part: str) -> BookCollection:
        """Поиск книг по части названия"""
        result = []
        for book in self.book_collection:
            if title_part.lower() in book.title.lower():
                result.append(book)
        return BookCollection(result)

    def get_all_books(self) -> BookCollection:
        """Получение всех книг"""
        return self.book_collection

    def update_book(self, old_isbn: str, new_book: 'Book') -> bool:
        """Обновление информации о книге"""
        old_book = self.find_by_isbn(old_isbn)
        if old_book:
            self.remove_book(old_book)
            self.add_book(new_book)
            return True
        return False

    def get_statistics(self) -> dict:
        """Получение статистики библиотеки"""
        return {
            'total_books': len(self.book_collection),
            'total_authors': len(self.index_dict._index_by_author),
            'years_range': list(self.index_dict._index_by_year.keys()),
            'genres': list(self.index_dict._index_by_genre.keys())
        }