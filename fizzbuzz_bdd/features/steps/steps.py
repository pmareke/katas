from behave import given, when, then
from behave.runner import Context
from expects import equal, expect
from fizzbuzz_bdd.main import FizzBuzz


@given('the number "{number}"')
def number(context: Context, number: int) -> None:
    context.number = int(number)


@when("calculates the result")
def calculates(context: Context) -> None:
    context.result = FizzBuzz.calculates(num=context.number)


@then('the result should be "{result}"')
def validates(context: Context, result: str) -> None:
    expect(context.result).to(equal(result))
