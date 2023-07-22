import unittest
from Task import count_distinct_numbers

class TestDistinctNumbers(unittest.TestCase):
    def test_count_distinct_numbers(self):
        self.assertEqual(count_distinct_numbers(1, 0), 1)
        self.assertEqual(count_distinct_numbers(1, 1), 2)
        self.assertEqual(count_distinct_numbers(1, 2), 5)
        self.assertEqual(count_distinct_numbers(1, 3), 10)
        self.assertEqual(count_distinct_numbers(2, 3), 10)
        self.assertEqual(count_distinct_numbers(5, 5), 0)
        self.assertEqual(count_distinct_numbers(0, 10), 4608)
        self.assertEqual(count_distinct_numbers(3, 6), 136)

if __name__ == '__main__':
    unittest.main()