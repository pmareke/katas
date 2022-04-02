from string_calculator import StringCalculator


class TestStringCalculator:
    def test_sum_two_numbers(self):
        assert StringCalculator().add(1, 1) == 2
