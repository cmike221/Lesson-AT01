import unittest
from main import remainder


class TestRemainder(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(20, 6), 2)

    def test_negative_numbers(self):
        self.assertEqual(remainder(-10, 3), 2)
        self.assertEqual(remainder(10, -3), -2)
        self.assertEqual(remainder(-10, -3), -1)

    def test_zero_dividend(self):
        self.assertEqual(remainder(0, 5), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            remainder(10, 0)
        self.assertEqual(str(context.exception), "Деление на ноль недопустимо.")

    def test_large_numbers(self):
        self.assertEqual(remainder(123456789, 10), 9)


if __name__ == '__main__':
    unittest.main()
