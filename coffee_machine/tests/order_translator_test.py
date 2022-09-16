from expects import expect, equal
from coffee_machine.src.order_translator import OrderTranslator
from coffee_machine.src.domain.order import Order


class TestOrderTranslator:
    def test_receives_an_order(self) -> None:
        order_translator = OrderTranslator()
        order = Order(type="T", sugar=1)

        command = order_translator.translate(order)

        expect(command).to(equal("T:1:0"))

    def test_receives_an_order_without_sugar(self) -> None:
        order_translator = OrderTranslator()
        order = Order(type="H", sugar=0)

        command = order_translator.translate(order)

        expect(command).to(equal("H::"))

    def test_receives_an_order_with_two_sugars(self) -> None:
        order_translator = OrderTranslator()
        order = Order(type="C", sugar=2)

        command = order_translator.translate(order)

        expect(command).to(equal("C:2:0"))
