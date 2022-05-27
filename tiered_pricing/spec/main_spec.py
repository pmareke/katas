from mamba import description, it
from expects import expect, equal, raise_error
from src.main import Subscription, InvalidSubscriptionNumber

with description("Tiered Pricing") as self:
    with it("a valid numnber of subscriptions"):
        tt = [
            {"subscriptions": 1, "total": 299},
            {"subscriptions": 2, "total": 598},
            {"subscriptions": 3, "total": 717},
            {"subscriptions": 4, "total": 956},
            {"subscriptions": 5, "total": 1195},
            {"subscriptions": 11, "total": 2409},
            {"subscriptions": 12, "total": 2628},
            {"subscriptions": 13, "total": 2847},
            {"subscriptions": 26, "total": 5174},
            {"subscriptions": 27, "total": 5373},
            {"subscriptions": 28, "total": 5572},
            {"subscriptions": 50, "total": 9950},
            {"subscriptions": 51, "total": 7599},
            {"subscriptions": 52, "total": 7748},
        ]

        for tc in tt:
            subscription = Subscription(tc["subscriptions"])

            expect(subscription.calculate_total_price()).to(equal(tc["total"]))

    with it("an invalid number of subscriptions"):
        expect(lambda: Subscription(-1)).to(raise_error(InvalidSubscriptionNumber))
