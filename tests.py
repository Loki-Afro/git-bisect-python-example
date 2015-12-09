#tests.py
import unittest
from add_two_numbers import add_two_numbers

class TestsForAddFunction(unittest.TestCase):

    def test_zeros(self):
        result = add_two_numbers(0, 0)
        self.assertEqual(0, result)

if __name__ == '__main__':
    unittest.main()


