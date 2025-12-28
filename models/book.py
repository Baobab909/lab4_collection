class Book:
    """Класс книги с основными атрибутами"""

    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    def __repr__(self) -> str:
        """Магический метод для строкового представления книги"""
        return f"Book('{self.title}', '{self.author}', {self.year}, '{self.genre}', '{self.isbn}')"

    def __eq__(self, other) -> bool:
        """Проверка равенства двух книг (по ISBN)"""
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False

    def __contains__(self, item: str) -> bool:
        """Магический метод для проверки наличия подстроки в информации о книге"""
        search_text = f"{self.title} {self.author} {self.genre} {self.year} {self.isbn}"
        return item.lower() in search_text.lower()

    def get_info(self) -> dict:
        """Возвращает информацию о книге в виде словаря"""
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'genre': self.genre,
            'isbn': self.isbn
        }