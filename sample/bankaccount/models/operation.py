class Operation:
    """
    account_id : long
    amount : Decimal
    operation_type : Enum
    time : datetime
    """
    def __init__(self, account_id, amount, operation_type, time):
        self.account_id = account_id
        self.amount = amount
        self.operationType = operation_type
        self.time = time

    @staticmethod
    def create(account_id, amount, operation_type, time):
        amount_extracted = amount.get_amount()
        return Operation(account_id, amount_extracted, operation_type, time)

    def __eq__(self, other):
        """Return true if both object are equal"""
        if not isinstance(other, Operation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal"""
        return not self == other
