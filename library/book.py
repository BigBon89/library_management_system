class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f"id:{self.id} title:{self.title} author:{self.author} year:{self.year} status:{self.status}"