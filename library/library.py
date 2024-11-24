class Library:
    def __init__(self):
        self.books = []
        self.next_id = 1

    def __str__(self):
        return "\n".join(map(str, self.books)) if self.books else "Библиотека пуста."