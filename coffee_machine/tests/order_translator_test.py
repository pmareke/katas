import pytest

from expects import expect, equal
from coffee_machine.src.order_translator import OrderTranslator
from coffee_machine.src.domain.order import Order


class TestDrinkMaker:
    @pytest.mark.parametrize(
        "order,expect_command",
        [
            (Order(type="T", sugar=1), "T:1:0"),
            (Order(type="H", sugar=0), "H::"),
            (Order(type="C", sugar=2), "C:2:0"),
        ],
    )
    def test_receives_the_correct_instruction_for_a_given_drink(
        self, order: Order, expect_command: str
    ) -> None:
        order_translator = OrderTranslator()

        command = order_translator.translate(order)

        expect(command).to(equal(expect_command))
