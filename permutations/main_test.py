from typing import List

from expects import equal, expect
import pytest

from main import Permutations


@pytest.mark.parametrize(
    "input,output",
    [
        ("a", ["a"]),
        ("ab", ["ab", "ba"]),
        ("aabb", ["aabb", "abab", "abba", "baab", "baba", "bbaa"]),
    ],
)
class TestPermutastions:
    def test_permutates_a_word(self, input: str, output: List[str]) -> None:
        expect(Permutations.process(input)).to(equal(output))
