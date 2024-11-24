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

    def change_status(self, id: str, new_status: str) -> None:
        """Меняет статус книги по переданному индексу"""

        if not id.isnumeric():
            print("Неверно указан id")
            return

        id = int(id)

        new_status = new_status.lower()

        if new_status not in {"в наличии", "выдана"}:
            print("Неверно указан статус, используйте 'в наличии', 'выдана'")
            return

        for book in self.books:
            if book.id == id:
                book.status = new_status
                print(f"Статус книги с id={id} изменен на '{new_status}'")
                return

        print(f"Книги с id={id} не существует")

    def find_book(self, name: str) -> None:
        result = []
        for book in self.books:
            if book.title == name or book.author == name or (name.isnumeric() and book.year == int(name)):
                result.append(str(book))

        if result:
            print("\n".join(result))
            return

        print("Книга не найдена")
