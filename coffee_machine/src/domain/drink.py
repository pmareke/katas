from dataclasses import dataclass


@dataclass
class Drink:
    price: float
    name: str

    @property
    def initial(self) -> str:
        return self.name[:1]


class Coffee(Drink):
    def __init__(self) -> None:
        super().__init__(name="C", price=0.6)

    def __str__(self) -> str:
        return "Coffee"


class Chocolate(Drink):
    def __init__(self) -> None:
        super().__init__(name="H", price=0.5)

    def __str__(self) -> str:
        return "Chocolate"


class Tea(Drink):
    def __init__(self) -> None:
        super().__init__(name="T", price=0.4)

    def __str__(self) -> str:
        return "Tea"


class OrangeJuice(Drink):
    def __init__(self) -> None:
        super().__init__(name="O", price=0.6)

    def __str__(self) -> str:
        return "Orange Juice"


class Hot(Drink):
    def __init__(self, drink: Drink):
        super().__init__(name=f"{drink.name}h", price=drink.price)
