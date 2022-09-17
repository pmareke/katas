from coffee_machine.src.domain.order import Order


class OrderTranslator:
    def translate(self, order: Order) -> str:
        sugar_quantity = order.sugar if order.sugar > 0 else ""
        sticks_quantity = 0 if order.sugar >= 1 else ""
        return f"{order.drink.name}:{sugar_quantity}:{sticks_quantity}"
