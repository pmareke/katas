import pytest
from typing import List
from main import Potter


@pytest.mark.parametrize(
    "price,items",
    [
        (0, []),
        (8, [1]),
        (8, [1]),
        (8, [1]),
        (8, [1]),
        (8 * 3, [1, 1, 1]),
        (8 * 2 * 0.95, [0, 1]),
        (8 * 3 * 0.9, [0, 2, 4]),
        (8 * 4 * 0.8, [0, 1, 2, 4]),
        (8 * 5 * 0.75, [0, 1, 2, 3, 4]),
    ],
)
class TestPotter:
    def test_basics(self, price: int, items: List[int]) -> None:
        potter = Potter(items)
        assert price == potter.price()
