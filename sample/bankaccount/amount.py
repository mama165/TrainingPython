from decimal import Decimal

from sample.bankaccount.exceptions.negative_amount import AmountNegativeError


class Amount(object):
    def __init__(self, amount):
        decimal_amount = Decimal(amount)
        if decimal_amount < 0:
            raise AmountNegativeError(decimal_amount)
        else:
            self.amount = decimal_amount
