from dataclasses import dataclass


@dataclass
class Credit:
    _value: int = 0

    def add(self, credit: "Credit") -> None:
        self._value += credit.value

    @property
    def value(self) -> int:
        return self._value
