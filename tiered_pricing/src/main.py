import sys


class InvalidSubscriptionNumber(Exception):
    pass


class Subscription:
    def __init__(self, subscriptions: int) -> None:
        if subscriptions <= 0:
            raise InvalidSubscriptionNumber()
        self.subscriptions = subscriptions

    def calculate_total_price(self) -> int:
        return self.subscriptions * self.unit_price()

    # PRIVATE

    def unit_price(self) -> int:
        ranges = [
            {"min": 1, "max": 2, "unit_price": 299},
            {"min": 3, "max": 10, "unit_price": 239},
            {"min": 11, "max": 25, "unit_price": 219},
            {"min": 26, "max": 50, "unit_price": 199},
        ]
        MINIMUM_UNIT_PRICE = 149

        for r in ranges:
            if self.subscriptions in range(r["min"], r["max"] + 1):
                return r["unit_price"]
        return MINIMUM_UNIT_PRICE
