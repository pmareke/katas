from dataclasses import dataclass
from typing import List


@dataclass
class Potter:
    items: List[int]

    def calculate_total_price(self) -> int:
        return self._calculate_total_price(self.items)

    @staticmethod
    def _calculate_total_price(items: List[int]) -> int:
        unit_price = 8
        return sum((unit_price * qty for qty in items))
