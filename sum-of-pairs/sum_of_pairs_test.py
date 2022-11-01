from expects import equal, expect
import pytest

from sum_of_pairs import SumPairs


@pytest.mark.parametrize(
    "input_list,target,result",
    [
        ([11, 3, 7, 5], 10, [3, 7]),
        ([4, 3, 2, 3, 4], 6, [4, 2]),
        ([0, 0, -2, 3], 2, None),
        ([10, 5, 2, 3, 7, 5], 10, [3, 7]),
    ],
)
class TestSumPairs:

    def test_calculates_sum_of_pairs(self, input_list: list[int], target: int,
                                     result: list[int]) -> None:
        expect(SumPairs.process(input_list, target)).to(equal(result))
