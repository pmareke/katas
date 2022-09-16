from dataclasses import dataclass


@dataclass
class Order:
    type: str
    sugar: int
