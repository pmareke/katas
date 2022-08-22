from functools import partial
from typing import Callable


numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for number, value in numbers.items():
    exec(
        f"def {number}(fn: Callable = lambda x: x) -> Callable: return partial(fn, {value})"
    )


def plus(fn: Callable) -> Callable:
    return partial(lambda x, y: x + y, fn())  # type: ignore


def minus(fn: Callable) -> Callable:
    return partial(lambda x, y: y - x, fn())  # type: ignore


def times(fn: Callable) -> Callable:
    return partial(lambda x, y: x * y, fn())  # type: ignore


def divided_by(fn: Callable) -> Callable:
    return partial(lambda x, y: int(y / x), fn())  # type: ignore
