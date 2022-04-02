import re


class StringCalculator:
    @staticmethod
    def add(input: str) -> int:
        if input == "":
            return 0

        result = 0
        pattern = re.compile("(-?[0-9]){1,}")
        operators = re.finditer(pattern, input)
        for op in operators:
            num = int(op.group(0))
            if num < 0:
                raise Exception
            if num <= 1000:
                result += num

        return result
