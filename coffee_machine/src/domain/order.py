from dataclasses import dataclass

from coffee_machine.src.domain.drink import Drink


@dataclass
class Order:
    drink: Drink
    sugar: int
