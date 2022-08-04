import pytest
from expects import expect, equal

from app.domain.item import Item
from app.gilded_rose import GildedRose


class TestGildedRose:
    @pytest.mark.parametrize(
        "item",
        [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
        ],
    )
    def test_updates_item_quality(self, item: Item) -> None:
        items = [item]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        expect(0).to(equal(items[0].quality))
