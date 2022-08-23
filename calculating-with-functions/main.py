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

operations = {
    "plus": "x + y",
    "minus": "y - x",
    "times": "x * y",
    "divided_by": "int(y/x)",
}

for number, value in numbers.items():
    exec(
        f"def {number}(fn: Callable = lambda x: x) -> Callable: return partial(fn, {value})"
    )

for name, operation in operations.items():
    exec(
        f"def {name}(fn: Callable) -> Callable: return partial(lambda x, y: {operation}, fn())"
    )
