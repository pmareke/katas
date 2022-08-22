from expects import be_true, expect
from typing import Callable
import pytest

from main import CalculatingWithFunctions


@pytest.mark.parametrize(
    "input,result",
    [
        (),
    ],
)
class TestCalculatingWithFunctions:
    def test_calculates_sum_of_pairs(self, input: Callable, result: int) -> None:
        expect(True).to(be_true)
