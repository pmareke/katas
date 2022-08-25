from typing import List

from expects import contain, expect
import pytest

from permutations import Permutations


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
        permutations = Permutations()
        perms = permutations.process(input)
        for entry in output:
            expect(perms).to(contain(entry))
