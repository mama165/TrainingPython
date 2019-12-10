import unittest
from unittest.mock import MagicMock

from sample.bankaccount.services.account_service import AccountService
from sample.bankaccount.models.amount import Amount
from sample.bankaccount.services.date_service import DateService
from sample.bankaccount.exceptions.negative_amount import AmountNegativeError
from sample.bankaccount.models.operation import Operation
from sample.bankaccount.repositories.operation_repository import OperationRepository
from sample.bankaccount.models.operation_type import OperationType


class AccountServiceTest(unittest.TestCase):
    def setUp(self):
        self.operation_repository = OperationRepository()
        self.date_service = DateService()
        self.account_service = AccountService(self.operation_repository, self.date_service)

    def test_should_throw_exception_when_amount_negative(self):
        with self.assertRaises(AmountNegativeError) as error:
            self.account_service.deposit("9486563683673946", -4)
        self.assertEqual(error.exception.message, "The amount is a negative number : -4")

    def test_should_record_operation_when_deposit(self):
        self.operation_repository.add = MagicMock()
        self.account_service.deposit(9486563683673946, "4")
        operation_deposit = Operation(9486563683673946, Amount("4"), OperationType.DEPOSIT)
        self.operation_repository.add.assert_called_once_with(operation_deposit)
