from approvaltests.combination_approvals import verify_all_combinations

from app.domain.item_factory import ItemFactory
from app.gilded_rose import GildedRose


class TestGildedRose:

    def test_update_quality(self) -> None:
        verify_all_combinations(
            self._update_quality,
            [
                [
                    "foo",
                    "Aged Brie",
                    "Backstage passes to a TAFKAL80ETC concert",
                    "Sulfuras, Hand of Ragnaros",
                ],
                [0, 1, 49, 50],
                [-1, 0, 6, 11],
            ],
        )

    @staticmethod
    def _update_quality(name: str, quality: int, sell_in: int) -> str:
        item = ItemFactory.create_item(name, sell_in, quality)

        GildedRose.update_quality([item])

        return f"{item}"
