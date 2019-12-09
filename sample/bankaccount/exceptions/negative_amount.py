class AmountNegativeError(BaseException):
    def __init__(self, amount):
        self.message = "The amount is a negative number : " + str(amount)
