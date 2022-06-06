from typing import List


class Potter:
    @staticmethod
    def price(items: List[int]) -> int:
        UNIT_PRICE = 8

        if len(items) == 0:
            return 0

        return sum([UNIT_PRICE * qty for qty in items])
