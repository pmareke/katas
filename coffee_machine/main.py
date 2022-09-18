from coffee_machine.src.domain.money import Money
from coffee_machine.src.domain.order import Order
from coffee_machine.src.domain.drink import Tea
from coffee_machine.use_cases.coffee_machine_command_handler import (
    CoffeeMachineCommandHandler,
)
from coffee_machine.src.infrastructure.order_translator import OrderTranslator
from coffee_machine.src.infrastructure.drink_maker import DrinkMaker
from coffee_machine.src.infrastructure.custom_printer import CustomPrinter
from coffee_machine.src.infrastructure.email_notifier import EmailNotifier
from coffee_machine.src.infrastructure.beverage_quantity_checker import (
    BeverageQuantityChecker,
)


def main() -> None:
    tea_order = Order(Tea(), sugar=0)
    order_translator = OrderTranslator()
    drink_maker = DrinkMaker()
    printer = CustomPrinter()
    email_notifier = EmailNotifier()
    beverage_shortage_checker = BeverageQuantityChecker()

    command_handler = CoffeeMachineCommandHandler(
        order_translator,
        drink_maker,
        printer,
        email_notifier,
        beverage_shortage_checker,
    )

    command_handler.add_money(money=Money(0.4))
    command_handler.make_drink(tea_order)

    command_handler.create_report()


if __name__ == "__main__":
    main()
