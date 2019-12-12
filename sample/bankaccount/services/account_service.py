from decimal import Decimal

from sample.bankaccount.exceptions.not_enough_money import NotEnoughMoneyOnAccountError
from sample.bankaccount.models.amount import Amount
from sample.bankaccount.models.operation import Operation
from sample.bankaccount.models.operation_type import OperationType


class AccountService(object):
    def __init__(self, operation_repository, date_service):
        self.operation_repository = operation_repository
        self.date_service = date_service

    def deposit(self, account_id, value):
        amount = Amount.create(value)
        operation = Operation.create(account_id, amount, OperationType.DEPOSIT, self.date_service.get_date())
        self.operation_repository.add(operation)

    def withdraw(self, account_id, value):
        amount = Amount.create(value)
        amount_extracted = amount.get_amount()
        operations = self.operation_repository.find_all(account_id)
        balance = self.compute_balance(operations)

        if balance < amount_extracted:
            raise NotEnoughMoneyOnAccountError(amount_extracted)

        operation = Operation.create(account_id, amount, OperationType.WITHDRAWAL, self.date_service.get_date())
        self.operation_repository.add(operation)

    @staticmethod
    def compute_balance(operations):
        balance = Decimal(0)

        for operation in operations:
            if operation.operationType == OperationType.DEPOSIT:
                balance += operation.amount
            if operation.operationType == OperationType.WITHDRAWAL:
                balance -= operation.amount

        return balance
