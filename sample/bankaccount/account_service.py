from sample.bankaccount.amount import Amount
from sample.bankaccount.operation import Operation
from sample.bankaccount.operation_type import OperationType


class AccountService(object):
    def __init__(self, operation_repository, date_service):
        self.operation_repository = operation_repository
        self.date_service = date_service

    def deposit(self, account_id, value):
        amount = Amount(value)
        operation = Operation(account_id, amount, OperationType.DEPOSIT, self.date_service)
        self.operation_repository.add(operation)

    def withdraw(self, account_id, value):
        pass
