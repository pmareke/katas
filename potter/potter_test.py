import pytest

from expects import expect, equal
from potter.potter import Potter


@pytest.mark.parametrize(
    "expected_price,items",
    [
        (0, []),
        (8, [1]),
        (8, [0, 1]),
        (8, [0, 0, 1]),
        (8, [0, 0, 0, 1]),
        (8, [0, 0, 0, 0, 1]),
        # (8 * 2 * 0.95, [0, 1]),
        # (8 * 3 * 0.9, [0, 2, 4]),
        # (8 * 4 * 0.8, [0, 1, 2, 4]),
        # (8 * 5 * 0.75, [0, 1, 2, 3, 4]),
    ],
)
class TestPotter:

    def test_calculates_the_total_price(self, expected_price: int,
                                        items: list[int]) -> None:
        potter = Potter(items)

        total_price = potter.calculate_total_price()

        expect(expected_price).to(equal(total_price))
