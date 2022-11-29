from collections.abc import Callable

from expects import equal, expect
import pytest

from calculating_with_functions.calculating_with_functions import (
    divided_by,
    eight,
    five,
    four,
    minus,
    nine,
    plus,
    seven,
    six,
    three,
    times,
    two,
)


@pytest.mark.parametrize(
    "input_functions,result",
    [
        (seven(times(five())), 35),
        (four(plus(nine())), 13),
        (eight(minus(three())), 5),
        (six(divided_by(two())), 3),
        (eight(divided_by(three())), 2),
    ],
)
class TestCalculatingWithFunctions:

    def test_calculates_functions(self, input_functions: Callable,
                                  result: int) -> None:
        expect(input_functions()).to(equal(result))
