class InvalidMoneyException(Exception):
    pass


class Money:

    def __init__(self, amount: float) -> None:
        self._validate_amount(amount)
        self.amount = amount

    def add_money(self, money: "Money") -> None:
        self.amount += money.value

    def remove_money(self, money: "Money") -> None:
        self.amount -= money.value

    @property
    def value(self) -> float:
        return self.amount

    @staticmethod
    def _validate_amount(amount: float) -> None:
        if amount < 0:
            raise InvalidMoneyException("Invalid amount of money")

    def __str__(self) -> str:
        return f"{self.amount:.1f}"
