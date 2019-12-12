import unittest
from unittest.mock import patch

from sample.bankaccount.exceptions.not_enough_money import NotEnoughMoneyOnAccountError
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
        self.ACCOUNT_ID = "9486563683673946"
        self.mocked_date = "1424080802"

    """mock_add.assert_not_called() won't work
        use mock_add.call_count instead
        see : http://engineroom.trackmaven.com/blog/mocking-mistakes/
    """
    @patch("sample.bankaccount.repositories.operation_repository.OperationRepository.add")
    def test_should_throw_exception_on_deposit_when_amount_negative(self, mock_add):
        with self.assertRaises(AmountNegativeError) as error:
            self.account_service.deposit(self.ACCOUNT_ID, -4)

        self.assertTrue(mock_add.call_count == 0)
        self.assertEqual(error.exception.message, "The amount is a negative number : -4")

    @patch("sample.bankaccount.repositories.operation_repository.OperationRepository.add")
    @patch("sample.bankaccount.services.date_service.DateService.get_date")
    def test_should_record_operation_when_deposit(self, mock_date, mock_add):
        mock_date.return_value = self.mocked_date
        self.account_service.deposit(self.ACCOUNT_ID, "4")
        operation_deposit = Operation.create(self.ACCOUNT_ID, Amount.create("4"), OperationType.DEPOSIT,
                                             self.mocked_date)
        mock_add.assert_called_once_with(operation_deposit)

    def test_should_throw_exception_on_withdrawal_when_amount_negative(self):
        with self.assertRaises(AmountNegativeError) as error:
            self.account_service.withdraw(self.ACCOUNT_ID, -4)
        self.assertEqual(error.exception.message, "The amount is a negative number : -4")

    def test_should_record_operation_when_withdrawal(self):
        pass

    @patch("sample.bankaccount.repositories.operation_repository.OperationRepository.find_all")
    @patch("sample.bankaccount.services.date_service.DateService.get_date")
    def test_should_throw_exception_on_withdrawal_when_not_enough_money(self, mock_date, mock_find_all):
        mock_date.return_value = self.mocked_date
        operation_deposit = Operation.create(self.ACCOUNT_ID, Amount.create("4"), OperationType.DEPOSIT,
                                             self.mocked_date)
        operation_list = [operation_deposit]
        mock_find_all.return_value = operation_list

        with self.assertRaises(NotEnoughMoneyOnAccountError) as error:
            self.account_service.withdraw(self.ACCOUNT_ID, 10)
        # self.operation_repository.add.assert_not_called()
        self.assertEqual(error.exception.message, "Withdrawal impossible with amount : 10")


if __name__ == '__main__':
    unittest.main()
