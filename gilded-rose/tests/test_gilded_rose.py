from approvaltests.combination_approvals import verify_all_combinations
from app.domain.item import Item
from app.gilded_rose import GildedRose


class TestGildedRose:
    def test_update_quality(self) -> None:
        verify_all_combinations(
            self._update_quality,
            [
                ["foo"],
                [0],
                [0],
            ],
        )

    @staticmethod
    def _update_quality(name: str, quality: int, sell_in: int) -> str:
        items = [Item(name, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        return f"{gilded_rose.items[0]}"
