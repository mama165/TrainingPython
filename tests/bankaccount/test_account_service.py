import unittest

from sample.bankaccount.account_service import AccountService
from sample.bankaccount.date_service import DateService
from sample.bankaccount.exceptions.negative_amount import AmountNegativeError
from sample.bankaccount.operation_repository import OperationRepository


class AccountServiceTest(unittest.TestCase):
    def setUp(self):
        self.operation_repository = OperationRepository()
        self.date_service = DateService()

    def test_should_throw_exception_when_amount_negative(self):
        with self.assertRaises(AmountNegativeError) as error:
            account_service = AccountService(self.operation_repository, self.date_service)
            account_service.deposit("9486563683673946", -4)
        self.assertEqual(error.exception.message, "The amount is a negative number : -4")
