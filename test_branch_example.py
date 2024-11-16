# test_branch_example.py

import unittest
from branch_example import classify_number

class TestClassifyNumber(unittest.TestCase):
    def test_positive_even(self):
        self.assertEqual(classify_number(4), "Positive Even")

    def test_positive_odd(self):
        self.assertEqual(classify_number(9), "Positive Odd")

    def test_negative_even(self):
        self.assertEqual(classify_number(-4), "Negative Even")

    def test_negative_odd(self):
        self.assertEqual(classify_number(-9), "Negative Odd")

    def test_zero(self):
        self.assertEqual(classify_number(0), "Zero")

if __name__ == '__main__':
    unittest.main()
