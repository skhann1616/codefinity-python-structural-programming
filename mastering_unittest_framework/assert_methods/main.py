import unittest

def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def get_item(lst, index):
    if index < 0 or index >= len(lst):
        return None
    return lst[index]

def make_none():
    return None

class TestFunctions(unittest.TestCase):
    # Write your test methods below using assertEqual, assertNotEqual, assertTrue, assertFalse, assertIs, assertIsNone, assertIn, and assertIsInstance
    def test_add_equal(self):
        self.assertEqual(add(2, 3), 5)
    def test_add_not_equal(self):
        self.assertNotEqual(add(2,2),5)
    def test_is_even_true(self):
        self.assertTrue(is_even(4))
    def test_is_even_false(self):
        self.assertFalse(is_even(5))
    def test_get_item_is(self):
        self.assertIs(get_item([10, 20, 30], 1),20)
    def test_get_item_is_none(self):
        self.assertIsNone(get_item([1, 2, 3], 10))
    def test_in_list(self):
        self.assertIn(2,[1,2,3])
    def test_add_is_instance(self):
        self.assertIsInstance(add(1,2),int)

if __name__ == "__main__":
    unittest.main(argv=['first-arg-ignored'], exit=False)

