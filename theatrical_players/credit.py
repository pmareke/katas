class Credit:

    def __init__(self, value: int = 0) -> None:
        self.quantity = value

    def add(self, credit: "Credit") -> None:
        self.quantity += credit.quantity

    @property
    def value(self) -> int:
        return self.quantity
