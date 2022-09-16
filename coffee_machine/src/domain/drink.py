from dataclasses import dataclass


@dataclass
class Drink:
    price: float
    name: str


class Coffee(Drink):
    def __init__(self) -> None:
        super().__init__(name="C", price=0.6)


class Chocolate(Drink):
    def __init__(self) -> None:
        super().__init__(name="H", price=0.5)


class Tea(Drink):
    def __init__(self) -> None:
        super().__init__(name="T", price=0.4)
