from library.book import Book
import json


class Library:
    """Класс для управления библиотекой
    Методы возвращают результат в виде сообщения для пользователя"""

    def __init__(self):
        self.books = []
        self.next_id = 1

    def __str__(self):
        return "\n".join(map(str, self.books)) if self.books else "Библиотека пуста"

    def add_book(self, title: str, author: str, year: str) -> str:
        """Добавляет книгу"""

        if not year.isnumeric():
            return "Некорректный год издания"

        book = Book(self.next_id, title, author, int(year), "в наличии")
        self.books.append(book)

        self.next_id += 1

        return f"Книга '{title}' добавлена с id={self.next_id - 1}"

    def remove_book(self, id: str) -> str:
        """Удаляет книгу по переданному индексу"""

        if not id.isnumeric():
            return "Неверно указан id"

        id = int(id)

        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                return f"Книга '{book.title}' с id={book.id} удалена"

        return "Данной книги не существует"

    def change_status(self, id: str, new_status: str) -> str:
        """Меняет статус книги по переданному индексу"""

        if not id.isnumeric():
            return "Неверно указан id"

        id = int(id)

        new_status = new_status.lower()

        if new_status not in {"в наличии", "выдана"}:
            return "Неверно указан статус, используйте 'в наличии', 'выдана'"

        for book in self.books:
            if book.id == id:
                book.status = new_status
                return f"Статус книги с id={id} изменен на '{new_status}'"

        return f"Книги с id={id} не существует"

    def find_book(self, name: str) -> str:
        """Ищет книгу по <Имя книги/Автор/Год>, выводит все совпадения"""

        result = []
        name = name.lower()
        for book in self.books:
            if (book.title.lower() == name or
                    book.author.lower() == name or
                    (name.isnumeric() and book.year == int(name))):
                result.append(str(book))

        if result:
            return "Найденные книги:\n" + "\n".join(result)

        return "Книга не найдена"

    def save_to_file(self, filename: str) -> str:
        """Сохраняет библиотеку в файл JSON"""

        data = {
            "next_id": self.next_id,
            "books": [book.to_dict() for book in self.books],
        }

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return f"Библиотека сохранена в файл '{filename}'"

    def load_from_file(self, filename: str) -> str:
        """Загружает библиотеку из файла JSON"""

        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.next_id = data["next_id"]
                self.books = [Book.from_dict(book) for book in data["books"]]

            return f"Библиотека загружена из файла '{filename}'"
        except FileNotFoundError:
            return f"Файл '{filename}' не найден"
        except json.JSONDecodeError:
            return f"Ошибка чтения файла '{filename}'"
        except KeyError as e:
            return f"Ошибка в структуре данных: отсутствует ключ {e}"
