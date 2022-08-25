from string_calculator import StringCalculator
import pytest


class TestStringCalculator:
    @pytest.mark.parametrize(
        "input,result",
        [
            ("", 0),
            ("4", 4),
            ("1,2", 3),
            ("1,2,3,4,5,6,7,8,9", 45),
            ("1\n2,3", 6),
            ("//;\n1;2", 3),
            ("1001,2", 2),
            ("//[***]\n1***2***3", 6),
            ("//[*][%]\n1*2%3", 6),
            ("//[foo][bar]\n1foo2bar3", 6),
        ],
    )
    def test_sum_two_numbers(self, input: str, result: int) -> None:
        assert StringCalculator().add(input) == result

    @pytest.mark.parametrize(
        "input",
        [
            "1,-2,-3",
        ],
    )
    def test_sum_negative_numbers_raises_an_exception(self, input: str) -> None:
        with pytest.raises(Exception):
            StringCalculator().add(input)
