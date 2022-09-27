import re


class StringCalculator:

    @staticmethod
    def add(input_string: str) -> int:
        if input_string == "":
            return 0

        result = 0
        pattern = re.compile("(-?[0-9]){1,}")
        operators = re.finditer(pattern, input_string)
        for operator in operators:
            num = int(operator.group(0))
            if num < 0:
                raise Exception
            if num <= 1000:
                result += num

        return result
