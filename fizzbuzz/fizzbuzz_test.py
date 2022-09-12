from pytest_bdd import scenario, given, then, parsers
from expects import equal, expect
from fizzbuzz import FizzBuzz


@scenario("features/fizzbuzz.feature", "FizzBuzz")
def test_fizzbuzz() -> None:
    pass


@given(
    parsers.parse("calculating the FizzBuzz representation of {number}"),
    target_fixture="fizzbuzz",
)
def calculates(number: str) -> str:
    return FizzBuzz.calculates(num=int(number))


@then(parsers.parse("the representation should be {result}"))
def validates(fizzbuzz: str, result: str) -> None:
    expect(fizzbuzz).to(equal(result))
