from fizzbuzz import FizzBuzz
import pytest


class TestFizzBuzz:
    @pytest.mark.parametrize("num", [3, 6, 9])
    def test_return_fizz_if_the_number_is_divisible_by_3(self, num: int):
        assert FizzBuzz().calculate(num) == "Fizz"

    @pytest.mark.parametrize("num", [5, 10, 20])
    def test_return_buzz_if_the_number_is_divisible_by_5(self, num: int):
        assert FizzBuzz().calculate(num) == "Buzz"

    @pytest.mark.parametrize("num", [15, 30, 45])
    def test_return_fizzbuzz_if_the_number_is_divisible_by_3_and_5(self, num: int):
        assert FizzBuzz().calculate(num) == "FizzBuzz"

    @pytest.mark.parametrize("num", [2, 4, 8])
    def test_return_the_number_if_the_number_is_not_divisible_by_3_and_5(
        self, num: int
    ):
        assert FizzBuzz().calculate(num) == f"{num}"
