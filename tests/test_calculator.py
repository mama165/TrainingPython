import unittest

from sample.calculator import calculate


class CalculatorTest(unittest.TestCase):
    def test_should_calculate_sum(self):
        output = calculate(3, 4)
        expected = 7
        self.assertEqual(output, expected)

    def test_should_calculate_sum_not_equal(self):
        output = calculate(5, 8)
        expected = 10
        self.assertNotEqual(output, expected)

    def test_should_return_concatenation_with_strings(self):
        self.assertEqual(calculate("2", "3"), "23")
