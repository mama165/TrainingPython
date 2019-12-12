import unittest

from sample.bankaccount.exceptions.negative_amount import AmountNegativeError
from sample.bankaccount.models.amount import Amount


class AmountTest(unittest.TestCase):
    def test_should_throw_exception_when_amount_negative(self):
        for value in {"-4", "-5", "-6", "-7"}:
            with self.assertRaises(AmountNegativeError) as error:
                Amount.create(value)

            message_expected = "The amount is a negative number : " + value
            self.assertEqual(error.exception.message, message_expected)

    def test_should_validate_equal_amount(self):
        for value in {"4", "5", "6", "7"}:
            self.assertEqual(Amount.create(value), Amount.create(value))


if __name__ == '__main__':
    unittest.main()
