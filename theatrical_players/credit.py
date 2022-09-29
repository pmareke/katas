class Credit:

    def __init__(self, value: int = 0) -> None:
        self._value = value

    def add(self, credit: "Credit") -> None:
        self._value += credit.value

    @property
    def value(self) -> int:
        return self._value
