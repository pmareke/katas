from typing import List

from expects import contain, expect
import pytest

from permutations.permutations import Permutations


@pytest.mark.parametrize(
    "input_string,output",
    [
        ("a", ["a"]),
        ("ab", ["ab", "ba"]),
        ("aabb", ["aabb", "abab", "abba", "baab", "baba", "bbaa"]),
    ],
)
class TestPermutastions:
    def test_permutates_a_word(self, input_string: str, output: List[str]) -> None:
        permutations = Permutations()
        perms = permutations.process(input_string)
        for entry in output:
            expect(perms).to(contain(entry))
