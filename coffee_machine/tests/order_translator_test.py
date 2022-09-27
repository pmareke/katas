from expects import expect, equal
from coffee_machine.src.infrastructure.order_translator import OrderTranslator
from coffee_machine.tests.test_data import TestData


class TestOrderTranslator:

    def test_receives_an_order(self) -> None:
        order_translator = OrderTranslator()
        order = TestData.a_tea_order()

        command = order_translator.translate(order)

        expect(command).to(equal("T:1:0"))

    def test_receives_an_order_without_sugar(self) -> None:
        order_translator = OrderTranslator()
        chocolate_order_without_sugar = TestData.a_chocolate_order(sugar=0)

        command = order_translator.translate(chocolate_order_without_sugar)

        expect(command).to(equal("H::"))

    def test_receives_an_order_with_two_sugars(self) -> None:
        order_translator = OrderTranslator()
        coffee_order = TestData.a_coffee_order(sugar=2)

        command = order_translator.translate(coffee_order)

        expect(command).to(equal("C:2:0"))

    def test_receives_an_order_with_orange_juice(self) -> None:
        order_translator = OrderTranslator()
        orange_juice_order_without_sugar = TestData.an_orange_juice_order(
            sugar=0)

        command = order_translator.translate(orange_juice_order_without_sugar)

        expect(command).to(equal("O::"))

    def test_receives_an_order_with_hot_chocolate(self) -> None:
        order_translator = OrderTranslator()
        a_chocolate = TestData.a_chocolate()
        hot_chocolate_order = TestData.a_hot_drink_order(a_chocolate)

        command = order_translator.translate(hot_chocolate_order)

        expect(command).to(equal("Hh:1:0"))
