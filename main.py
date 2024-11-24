class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status


class Library:
    def __init__(self):
        self.books = []
        self.next_id = 1


def main():
    pass


if __name__ == '__main__':
    main()
