from dataclasses import dataclass

from bank.src.domain.amount import Amount


@dataclass
class Balance:
    total: int

    def increase(self, amount: Amount) -> None:
        self.total += amount.value

    def decrease(self, amount: Amount) -> None:
        self.total -= amount.value

    @property
    def value(self) -> int:
        return self.total
