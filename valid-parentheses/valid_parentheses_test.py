from expects import be, expect
import pytest

from valid_parentheses import ValidParentheses


@pytest.mark.parametrize(
    "input_message,is_valid",
    [
        ("()", True),
        (")(()))", False),
        ("(", False),
        ("(())((()())())", True),
    ],
)
class TestValidParentheses:
    def test_validates_the_parenthese(self, input_message: str, is_valid: bool) -> None:
        expect(ValidParentheses.is_valid(input_message)).to(be(is_valid))
