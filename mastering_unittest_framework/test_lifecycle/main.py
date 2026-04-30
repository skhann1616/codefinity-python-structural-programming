import unittest

class Book:
    def __init__(self, title, author, amount):
        self.title = title
        self.author = author
        self.amount = amount

    def __repr__(self):
        return f"<Book {self.title}, written by {self.author}, {self.amount} pieces>"

    def sale(self):
        if self.amount > 0:
            self.amount -= 1
        else:
            return "This book sold out"

# Write your code below:
class TestBook(unittest.TestCase):
        def setUp(self):
            self.book = Book("1984", "George Orwell", 2)
            
        def tearDown(self):
            print("Cleaning up after each test.")
            del self.book

        def test_sale(self):
            self.book.sale()
            assert self.book.sale() == "This book sold out"

        def test_book_repr(self):
            self.assertEqual(repr(self.book), "<Book 1984, written by George Orwell, 2 pieces>")