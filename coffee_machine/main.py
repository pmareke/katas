from coffee_machine.src.domain.money import Money
from coffee_machine.src.domain.order import Order
from coffee_machine.src.domain.drink import Tea
from coffee_machine.src.use_cases.coffee_machine_command_handler import (
    CoffeeMachineCommandHandlerFactory,
)


def main() -> None:
    tea_order = Order(Tea(), sugar=0)
    command_handler = CoffeeMachineCommandHandlerFactory.make()

    command_handler.add_money(money=Money(0.4))
    command_handler.make_drink(tea_order)

    command_handler.create_report()


if __name__ == "__main__":
    main()
