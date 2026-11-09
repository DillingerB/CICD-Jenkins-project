import unittest
from app import add_numbers
from app import sub_numbers

# Checks that add_numbers returns the expected sums.
class TestAddNumbers(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)

    def test_add_negative(self):
        self.assertEqual(add_numbers(-1, 1), 0)

    def test_Negative(self):
        self.assertEqual(add_numbers(-2, -1), -3)

# Checks that sub_numbers returns the expected sums.
class TestSubNumbers(unittest.TestCase):
    def test_subtract_positive(self):
        self.assertEqual(sub_numbers(2, 3), -1)
    def test_subtract_zero(self):
        self.assertEqual(sub_numbers(0, 0), 0)
    def test_subtract_negative(self):
        self.assertEqual(sub_numbers(-1, 1), -2)
    def test_positive_answer(self):
        self.assertEqual(sub_numbers(5, 3), 2)    

if __name__ == "__main__":
    unittest.main()