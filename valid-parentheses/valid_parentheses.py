from typing import List


class ValidParentheses:

    @staticmethod
    def is_valid(input_message: str) -> bool:
        stack: List[str] = []

        for parenthesis in input_message:
            if parenthesis == "(":
                stack.append(parenthesis)
            elif len(stack) == 0:
                return False
            else:
                stack.pop()

        return bool(len(stack) == 0)
