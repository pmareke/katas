from typing import List


class RangeExtraction:
    def __init__(self, input: List[int]):
        self.input = input

    def extract(self) -> str:
        ranges: List[str] = []
        current_range: List[int] = []
        for index, number in enumerate(self.input):
            if len(current_range) == 0:  # First element or after starting a new range
                current_range = [number]
            if index == len(self.input) - 1:  # Last element
                string_range = self._calculate_string_range(current_range)
                ranges.append(string_range)
                break
            if number + 1 != self.input[index + 1]:  # Next element is not consecutive
                string_range = self._calculate_string_range(current_range)
                ranges.append(string_range)
                current_range = [self.input[index + 1]]
            else:  # Next number is consecutive
                current_range.append(number + 1)
        return ",".join(ranges)

    def _calculate_string_range(self, range_list: List[int]) -> str:
        first = range_list[0]
        last = range_list[-1]
        separator = "-" if len(range_list) > 2 else ","
        r = f"{first}" if len(range_list) == 1 else f"{first}{separator}{last}"
        return r
