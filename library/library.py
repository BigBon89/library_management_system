from library.book import Book


class Library:
    def __init__(self):
        self.books = []
        self.next_id = 1

    def __str__(self):
        return "\n".join(map(str, self.books)) if self.books else "Библиотека пуста."

    def add_book(self, title: str, author: str, year: str) -> None:
        """Добавляет книгу"""

        if not year.isnumeric():
            print("Некорректный год издания")
            return

        book = Book(self.next_id, title, author, int(year), "в наличии")
        self.books.append(book)

        print(f"Книга '{title}' добавлена с id={self.next_id}")

        self.next_id += 1

    def remove_book(self, id: str) -> None:
        """Удаляет книгу по переданному индексу"""

        if not id.isnumeric():
            print("Неверно указан id")
            return

        id = int(id)

        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                return
        
        print("Данной книги не существует")