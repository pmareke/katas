from coffee_machine.src.domain.order import Order
from coffee_machine.src.domain.drink import (
    Drink,
    Chocolate,
    Coffee,
    Tea,
    OrangeJuice,
    Water,
    Milk,
    Hot,
)


class TestData:

    @staticmethod
    def a_tea_order(sugar: int = 1) -> Order:
        return Order(Tea(), sugar)

    @staticmethod
    def a_coffee_order(sugar: int = 1) -> Order:
        return Order(Coffee(), sugar=sugar)

    @staticmethod
    def a_chocolate_order(sugar: int = 1) -> Order:
        return Order(Chocolate(), sugar=sugar)

    @staticmethod
    def an_orange_juice_order(sugar: int = 1) -> Order:
        return Order(OrangeJuice(), sugar=sugar)

    @staticmethod
    def a_hot_drink_order(drink: Drink, sugar: int = 1) -> Order:
        return Order(Hot(drink), sugar=sugar)

    @staticmethod
    def a_water() -> Water:
        return Water()

    @staticmethod
    def a_milk() -> Milk:
        return Milk()

    @staticmethod
    def a_chocolate() -> Chocolate:
        return Chocolate()
