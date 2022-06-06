from typing import List


class Potter:
    def __init__(self, items: List[int]) -> None:
        self.items = items

    def price(self) -> int:
        return self._calculate_total_price(self.items)

    @staticmethod
    def _calculate_total_price(items: List[int]) -> int:
        UNIT_PRICE = 8
        return sum([UNIT_PRICE * qty for qty in items])
