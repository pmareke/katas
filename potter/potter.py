from dataclasses import dataclass


@dataclass
class Potter:
    items: list[int]

    def calculate_total_price(self) -> int:
        return self._calculate_total_price(self.items)

    @staticmethod
    def _calculate_total_price(items: list[int]) -> int:
        unit_price = 8
        return sum(unit_price * qty for qty in items)
