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


class OrangeJuice(Drink):
    def __init__(self) -> None:
        super().__init__(name="O", price=0.6)


class Hot(Drink):
    def __init__(self, drink: Drink):
        super().__init__(name=f"{drink.name}h", price=drink.price)
