from typing import List


class ValidParentheses:
    @staticmethod
    def is_valid(input: str) -> bool:
        stack: List[str] = []

        for parenthesis in input:
            if parenthesis == "(":
                stack.append(parenthesis)
            elif len(stack) == 0:
                return False
            else:
                stack.pop()

        return True if len(stack) == 0 else False
