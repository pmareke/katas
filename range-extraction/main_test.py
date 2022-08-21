import pytest
from expects import expect, equal
from typing import List
from main import RangeExtraction


@pytest.mark.parametrize(
    "input,output",
    [
        ([], []),
    ],
)
class TestRangeExtraction:
    def test_extracts_a_range(self, input: List[int], output: List[int]) -> None:
        expect(RangeExtraction.extract(input)).to(equal(output))
