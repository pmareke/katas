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
    ],
)
class TestPotter:
    def test_basics(self, price: int, items: List[int]) -> None:
        assert price, Potter.price(items)
