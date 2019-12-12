class NotEnoughMoneyOnAccountError(BaseException):
    def __init__(self, amount):
        self.message = "Withdrawal impossible with amount : " + str(amount)
