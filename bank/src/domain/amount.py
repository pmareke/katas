class InvalidAmountException(Exception):
    pass


class Amount:

    def __init__(self, amount: int) -> None:
        self._validate_amount(amount)
        self._amount = amount

    @property
    def value(self) -> int:
        return self._amount

    @staticmethod
    def _validate_amount(amount: int) -> None:
        if amount < 0:
            raise InvalidAmountException("The amount should be positive")
