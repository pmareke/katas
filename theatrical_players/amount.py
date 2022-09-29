from dataclasses import dataclass


@dataclass
class Amount:
    value: int

    def __add__(self, another: "Amount") -> "Amount":
        return Amount(self.value + another.value)

    @property
    def format(self) -> str:
        return f"${self.value/100:0,.2f}"
