import unittest

from sample.bankaccount.amount import Amount
from sample.bankaccount.exceptions.negative_amount import AmountNegativeError


class AmountTest(unittest.TestCase):
    def test_should_throw_exception_when_amount_negative(self):
        with self.assertRaises(AmountNegativeError) as error:
            Amount("-4")
        self.assertEqual(error.exception.message, "The amount is a negative number : -4")


if __name__ == '__main__':
    unittest.main()
