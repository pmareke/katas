from coffee_machine.src.domain.order import Order
from coffee_machine.src.order_translator import OrderTranslator
from coffee_machine.src.drink_maker import DrinkMaker


class CoffeeMachine:
    def __init__(self, order_translator: OrderTranslator, drink_maker: DrinkMaker):
        self.order_translator = order_translator
        self.drink_maker = drink_maker
        self.money = 0.0

    def add_money(self, money: float) -> None:
        self.money = money

    def translate_order(self, order: Order) -> str:
        if self.money < order.drink.price:
            missing_money = round(abs(self.money - order.drink.price), 2)
            return f"M:Sorry there is not enough money in the cofee machine, you need {missing_money} more."

        return str(self.order_translator.translate(order))

    def make_drink(self, command: str) -> None:
        self.drink_maker.make(command)
