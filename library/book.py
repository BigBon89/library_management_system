class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f"id:{self.id} title:{self.title} author:{self.author} year:{self.year} status:{self.status}"

    def to_dict(self) -> dict:
        """Преобразует объект книги в словарь"""

        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: dict):
        """Создает объект книги из словаря"""

        return Book(data["id"], data["title"], data["author"], data["year"], data["status"])
