from enum import Enum


class RomanNumerals:
    @staticmethod
    def calculate(value: int) -> str:
        result = ""
        for roman in RomanToArabic:
            while value >= roman.value:
                result += roman.name
                value -= roman.value
        return result


class RomanToArabic(Enum):
    M = 1000
    CM = 900
    D = 500
    CD = 400
    C = 100
    XC = 90
    L = 50
    XL = 40
    X = 10
    IX = 9
    V = 5
    IV = 4
    I = 1  # noqa: E741
