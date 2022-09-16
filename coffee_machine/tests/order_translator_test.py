from expects import expect, equal
from coffee_machine.src.order_translator import OrderTranslator
from coffee_machine.src.domain.order import Order
from coffee_machine.src.domain.drink import Hot, Coffee, Chocolate, Tea, OrangeJuice


class TestOrderTranslator:
    def test_receives_an_order(self) -> None:
        order_translator = OrderTranslator()
        order = Order(Tea(), sugar=1)

        command = order_translator.translate(order)

        expect(command).to(equal("T:1:0"))

    def test_receives_an_order_without_sugar(self) -> None:
        order_translator = OrderTranslator()
        order = Order(Chocolate(), sugar=0)

        command = order_translator.translate(order)

        expect(command).to(equal("H::"))

    def test_receives_an_order_with_two_sugars(self) -> None:
        order_translator = OrderTranslator()
        order = Order(Coffee(), sugar=2)

        command = order_translator.translate(order)

        expect(command).to(equal("C:2:0"))

    def test_receives_an_order_with_orange_juice(self) -> None:
        order_translator = OrderTranslator()
        order = Order(OrangeJuice(), sugar=0)

        command = order_translator.translate(order)

        expect(command).to(equal("O::"))

    def test_receives_an_order_with_hot_chocolate(self) -> None:
        order_translator = OrderTranslator()
        order = Order(Hot(Chocolate()), sugar=1)

        command = order_translator.translate(order)

        expect(command).to(equal("Hh:1:0"))
