from behave import given, when, then
from expects import equal, expect
from fizzbuzz_bdd.main import FizzBuzz


@given('the number "{number}"')
def step_impl(context, number: int) -> None:
    context.number = int(number)


@when("calculates the result")
def step_impl(context) -> None:
    context.result = FizzBuzz.calculates(num=context.number)


@then('the result should be "{result}"')
def step_impl(context, result: str) -> None:
    expect(context.result).to(equal(result))
