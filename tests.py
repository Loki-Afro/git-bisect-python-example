#tests.py
import unittest
from add_two_numbers import add_two_numbers

class TestsForAddFunction(unittest.TestCase):

    def test_zeros(self):
        result = add_two_numbers(0, 0)
        self.assertEqual(0, result)

    def test_basic_addition(self):
        result = add_two_numbers(4, 6)
        self.assertEqual(10, result)

    def test_basic_addition2(self):
        result = add_two_numbers(-6, 999)
        self.assertEqual(993, result)



if __name__ == '__main__':
    unittest.main()


