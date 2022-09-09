from dataclasses import dataclass
from typing import List


@dataclass
class Potter:
    items: List[int]

    def price(self) -> int:
        return self._calculate_total_price(self.items)

    @staticmethod
    def _calculate_total_price(items: List[int]) -> int:
        UNIT_PRICE = 8
        return sum([UNIT_PRICE * qty for qty in items])
