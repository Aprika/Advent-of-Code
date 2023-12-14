class Account:
    def __init__(self):
        self._balance = 0

    @property
    def get_balance(self):
        return self._balance

    @get_balance.setter
    def get_balance(self, amount):