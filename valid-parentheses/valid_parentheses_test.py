from expects import be, expect
import pytest

from valid_parentheses import ValidParentheses


@pytest.mark.parametrize(
    "input,is_valid",
    [
        ("()", True),
        (")(()))", False),
        ("(", False),
        ("(())((()())())", True),
    ],
)
class TestValidParentheses:
    def test_validates_the_parenthese(self, input: str, is_valid: bool) -> None:
        expect(ValidParentheses.is_valid(input)).to(be(is_valid))
