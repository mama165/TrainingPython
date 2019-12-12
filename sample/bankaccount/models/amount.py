from decimal import Decimal

from sample.bankaccount.exceptions.negative_amount import AmountNegativeError

"""
amount : Decimal
"""


class Amount(object):
    def __init__(self, amount):
        self.amount = amount

    @staticmethod
    def create(amount):
        decimal_amount = Decimal(amount)
        if decimal_amount < 0:
            raise AmountNegativeError(decimal_amount)
        else:
            return Amount(decimal_amount)

    def get_amount(self):
        return self.amount

    def __eq__(self, other):
        if not isinstance(other, Amount):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal"""
        return not self == other
