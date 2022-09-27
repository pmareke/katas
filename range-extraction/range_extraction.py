from dataclasses import dataclass
from typing import List


@dataclass
class RangeExtraction:
    input: List[int]

    def process(self) -> str:
        string_ranges: List[str] = []
        current_range: List[int] = []
        for index, number in enumerate(self.input):
            if len(current_range
                  ) == 0:  # First element or after starting a new range
                current_range = [number]
            if index == len(self.input) - 1:  # Last element
                string_range = self._calculate_string_range(current_range)
                string_ranges.append(string_range)
                break
            if number + 1 != self.input[index +
                                        1]:  # Next element is not consecutive
                string_range = self._calculate_string_range(current_range)
                string_ranges.append(string_range)
                current_range = [self.input[index + 1]]
            else:  # Next number is consecutive
                current_range.append(number + 1)
        return ",".join(string_ranges)

    def _calculate_string_range(self, current_range: List[int]) -> str:
        first = current_range[0]
        last = current_range[-1]
        separator = "-" if len(current_range) > 2 else ","
        return f"{first}" if len(
            current_range) == 1 else f"{first}{separator}{last}"
