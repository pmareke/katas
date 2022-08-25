from expects import equal, expect
import pytest

from fizzbuzz import FizzBuzz


class TestFizzBuzz:
    @pytest.mark.parametrize("num", [3, 6, 9])
    def test_return_fizz_if_the_number_is_divisible_by_3(self, num: int) -> None:
        expect(FizzBuzz().calculate(num)).to(equal("Fizz"))

    @pytest.mark.parametrize("num", [5, 10, 20])
    def test_return_buzz_if_the_number_is_divisible_by_5(self, num: int) -> None:
        expect(FizzBuzz().calculate(num)).to(equal("Buzz"))

    @pytest.mark.parametrize("num", [15, 30, 45])
    def test_return_fizzbuzz_if_the_number_is_divisible_by_3_and_5(
        self, num: int
    ) -> None:
        expect(FizzBuzz().calculate(num)).to(equal("FizzBuzz"))

    @pytest.mark.parametrize("num", [2, 4, 8])
    def test_return_the_number_if_the_number_is_not_divisible_by_3_and_5(
        self, num: int
    ) -> None:
        expect(FizzBuzz().calculate(num)).to(equal(f"{num}"))
