from datetime import datetime
import unittest

from sample.bankaccount.models.amount import Amount
from sample.bankaccount.models.operation import Operation
from sample.bankaccount.models.operation_type import OperationType


class OperationTest(unittest.TestCase):
    def test_should_validate_equal_operation(self):
        o1 = Operation.create("9486563683673946", Amount(4), OperationType.DEPOSIT, datetime.fromtimestamp(1424080802))
        o2 = Operation.create("9486563683673946", Amount(4), OperationType.DEPOSIT, datetime.fromtimestamp(1424080802))

        self.assertEqual(o1, o2)


if __name__ == '__main__':
    unittest.main()
