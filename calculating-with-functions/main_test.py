from expects import be_true, expect, equal
from typing import Callable
import pytest

from main import (
    seven,
    times,
    five,
    four,
    plus,
    nine,
    eight,
    minus,
    three,
    six,
    divided_by,
    two,
)


@pytest.mark.parametrize(
    "input,result",
    [
        (seven(times(five())), 35),
        (four(plus(nine())), 13),
        (eight(minus(three())), 5),
        (six(divided_by(two())), 3),
        (eight(divided_by(three())), 2),
    ],
)
class TestCalculatingWithFunctions:
    def test_calculates_functions(self, input: Callable, result: int) -> None:
        expect(input()).to(equal(result))
