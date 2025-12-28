from models.book import Book
from models.library import Library
from biblio import LibrarySimulation


def create_library() -> Library:
    """Создание библиотеки с начальными книгами"""
    library = Library("Библиотека")

    # Добавление начальных книг
    initial_books = [
        Book("Война и мир", "Лев Толстой", 1869, "Роман", "978-5-699-12014-7"),
        Book("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", "978-5-17-090324-7"),
        Book("1984", "Джордж Оруэлл", 1949, "Антиутопия", "978-5-17-090325-4"),
        Book("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", "978-5-17-090326-1"),
        Book("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "Фэнтези", "978-5-389-07435-4"),
        Book("Властелин колец", "Джон Толкин", 1954, "Фэнтези", "978-5-17-090327-8"),
        Book("Маленький принц", "Антуан де Сент-Экзюпери", 1943, "Повесть", "978-5-699-12015-4"),
        Book("Анна Каренина", "Лев Толстой", 1877, "Роман", "978-5-17-090328-5"),
    ]

    for book in initial_books:
        library.add_book(book)

    print(f"Создана библиотека: {library}")
    print(f"Начальное количество книг: {len(library.book_collection)}")
    return library


def demonstrate_collections(library: Library):
    """Демонстрация работы пользовательских коллекций"""
    print("\nДЕМОНСТРАЦИЯ ПОЛЬЗОВАТЕЛЬСКИХ КОЛЛЕКЦИЙ")
    print("\n1. BookCollection (списковая коллекция):")
    print(f"   Длина коллекции: {len(library.book_collection)}")
    print(f"   Первые 3 книги (срез): {library.book_collection[:3]}")
    print("   Итерация (первые 3 книги):")
    for i, book in enumerate(library.book_collection):
        if i >= 3:
            break
        print(f"     - {book.title}")
    print(f"   'Толстой' в коллекции? {'Толстой' in library.book_collection}")

    print("\n2. IndexDict (словарная коллекция):")
    print(f"   Книг в индексе: {len(library.index_dict)}")

    # Поиск по разным критериям
    print("   Поиск по автору 'Лев Толстой':")
    books_by_tolstoy = library.index_dict[('author', 'Лев Толстой')]
    for book in books_by_tolstoy:
        print(f"     - {book.title} ({book.year})")

    print("   Поиск по году 1869:")
    books_1869 = library.index_dict[('year', 1869)]
    for book in books_1869:
        print(f"     - {book.title} - {book.author}")

    print("   Поиск по ISBN:")
    book_by_isbn = library.index_dict["978-5-699-12014-7"]
    print(f"     - {book_by_isbn.title}")


def demonstrate_library_functionality(library: Library):
    """Демонстрация функциональности библиотеки"""
    print("\nДЕМОНСТРАЦИЯ ФУНКЦИОНАЛЬНОСТИ БИБЛИОТЕКИ")

    # Поиск книг
    print("\n1. Поиск книг по автору 'Лев Толстой':")
    tolstoy_books = library.find_by_author("Лев Толстой")
    for book in tolstoy_books:
        print(f"   - {book.title} ({book.year})")

    print("\n2. Поиск книг по жанру 'Фэнтези':")
    fantasy_books = library.find_by_genre("Фэнтези")
    for book in fantasy_books:
        print(f"   - {book.title} - {book.author}")

    print("\n3. Поиск книг по году 1869:")
    books_1869 = library.find_by_year(1869)
    for book in books_1869:
        print(f"   - {book.title} - {book.author}")

    # Добавление и удаление
    print("\n4. Добавление новой книги:")
    new_book = Book("Новая книга", "Новый автор", 2023, "Научная", "NEW-001")
    if library.add_book(new_book):
        print(f"   Добавлена: {new_book.title}")

    print("\n5. Удаление книги:")
    if library.remove_book(new_book):
        print(f"   Удалена: {new_book.title}")


def main():
    """Основная функция программы"""
    #Создание библиотеки
    library = create_library()
    #Демонстрация коллекций
    demonstrate_collections(library)
    #Демонстрация функциональности
    demonstrate_library_functionality(library)
    # Запуск симуляции
    print("ЗАПУСК СИМУЛЯЦИИ")
    simulation = LibrarySimulation(library)
    # C seed
    simulation.run_simulation(steps=15, seed=42)
    # Без seed
    simulation2 = LibrarySimulation(library)
    simulation2.run_simulation(steps=10)
if __name__ == "__main__":
    main()