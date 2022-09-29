class Amount:

    def __init__(self, value: int = 0) -> None:
        self.value = value

    def __add__(self, another: "Amount") -> "Amount":
        return Amount(self.value + another.value)

    def add(self, amount: "Amount") -> None:
        self.value += amount.value

    @property
    def format(self) -> str:
        return f"${self.value/100:0,.2f}"
