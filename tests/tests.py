import unittest

from library.library import Library


class Tests(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book_valid(self):
        self.library.add_book("Книга 1", "Автор 1", "2019")
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].id, 1)
        self.assertEqual(self.library.books[0].title, "Книга 1")
        self.assertEqual(self.library.books[0].author, "Автор 1")
        self.assertEqual(self.library.books[0].year, 2019)

    def test_add_book_invalid_year(self):
        self.library.add_book("Книга 1", "Автор 1", "год")
        self.assertEqual(len(self.library.books), 0)

    def test_remove_book_valid(self):
        self.library.add_book("Книга 1", "Автор 1", "2019")
        self.library.remove_book("1")
        self.assertEqual(len(self.library.books), 0)

    def test_remove_book_invalid_id(self):
        self.library.add_book("Книга 1", "Автор 1", "2019")
        self.library.remove_book("2")
        self.assertEqual(len(self.library.books), 1)

    def test_change_status_valid(self):
        self.library.add_book("Книга 1", "Автор 1", "2019")
        self.library.change_status("1", "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")

    def test_change_status_invalid_status(self):
        self.library.add_book("Книга 1", "Автор 1", "2019")
        self.library.change_status("1", "что-то")
        self.assertEqual(self.library.books[0].status, "в наличии")

    def test_save_and_load_library(self):
        self.library.add_book("Книга 1", "Автор 1", "2019")
        self.library.save_to_file("test_library.json")

        new_library = Library()
        new_library.load_from_file("test_library.json")
        self.assertEqual(len(new_library.books), 1)
        self.assertEqual(new_library.books[0].title, "Книга 1")
        self.assertEqual(new_library.books[0].author, "Автор 1")
        self.assertEqual(new_library.books[0].year, 2019)
