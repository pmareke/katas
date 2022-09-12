from pytest_bdd import scenario, given, then, parsers
from expects import equal, expect
from fizzbuzz import FizzBuzz


@scenario("features/fizzbuzz.feature", "FizzBuzz")
def test_fizzbuzz() -> None:
    pass


@given(
    parsers.parse("calculating the FizzBuzz representation of {number:d}"),
    target_fixture="fizzbuzz",
)
def calculates(number: int) -> str:
    return FizzBuzz.calculates(num=number)


@then(parsers.parse("the representation should be {result}"))
def validates(fizzbuzz: str, result: str) -> None:
    expect(fizzbuzz).to(equal(result))
