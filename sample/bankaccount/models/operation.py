class Operation:
    def __init__(self, account_id, amount, operation_type):
        self.account_id = account_id
        self.amount = amount
        self.operationType = operation_type
        # self.time = time

    def __eq__(self, other):
        """Return true if both object are equal"""
        if not isinstance(other, Operation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal"""
        return not self == other
