from expects import expect, equal
from typing import List

import pytest

from potter import Potter


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
    def test_basics(self, expected_price: int, items: List[int]) -> None:
        potter = Potter(items)

        total_price = potter.calculate_total_price()

        expect(expected_price).to(equal(total_price))
