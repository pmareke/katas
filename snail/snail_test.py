from typing import List

from expects import equal, expect
import pytest

from snail.snail import Snail


@pytest.mark.parametrize(
    "input_list,output",
    [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        ),
        (
            [[1, 2, 3], [8, 9, 4], [7, 6, 5]],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ),
    ],
)
class TestSnail:
    def test_snails_an_array(
        self, input_list: List[List[int]], output: List[int]
    ) -> None:
        expect(Snail.process(input_list)).to(equal(output))
