from typing import List

from expects import equal, expect
import pytest

from main import SumPairs


@pytest.mark.parametrize(
    "input,sum",
    [([11, 3, 7, 5], 10)],
)
class TestSumPairs:
    def test_calculates_sum_of_pairs(self, input: List[int], sum: int) -> None:
        expect(SumPairs.process(input, sum)).to(equal(sum))
