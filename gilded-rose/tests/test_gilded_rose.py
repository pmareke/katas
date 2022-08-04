import pytest
from expects import expect, equal

from app.domain.item import Item
from app.gilded_rose import GildedRose


class TestGildedRose:
    @pytest.mark.parametrize(
        "item,quantity",
        [
            (Item(name="+5 Dexterity Vest", sell_in=10, quality=20), 19),
            (Item(name="Aged Brie", sell_in=2, quality=0), 1),
            (Item(name="Elixir of the Mongoose", sell_in=5, quality=7), 6),
            (Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80), 80),
            (Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80), 80),
            (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20), 21),
            (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49), 50),
            (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49), 50),
            (Item(name="Conjured Mana Cake", sell_in=3, quality=6), 5),  # <-- :O
        ],
    )
    def test_updates_item_quality_one_time(self, item: Item, quantity: int) -> None:
        items = [item]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        expect(quantity).to(equal(items[0].quality))

    @pytest.mark.parametrize(
        "item,quantity",
        [
            (Item(name="+5 Dexterity Vest", sell_in=10, quality=20), 18),
            (Item(name="Aged Brie", sell_in=2, quality=0), 2),
            (Item(name="Elixir of the Mongoose", sell_in=5, quality=7), 5),
            (Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80), 80),
            (Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80), 80),
            (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20), 22),
            (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49), 50),
            (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49), 50),
            (Item(name="Conjured Mana Cake", sell_in=3, quality=6), 4),  # <-- :O
        ],
    )
    def test_updates_item_quality_two_times(self, item: Item, quantity: int) -> None:
        items = [item]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        gilded_rose.update_quality()

        expect(quantity).to(equal(items[0].quality))

    @pytest.mark.parametrize(
        "item,quantity",
        [
            (Item(name="+5 Dexterity Vest", sell_in=10, quality=20), 17),
            (Item(name="Aged Brie", sell_in=2, quality=0), 4),
            (Item(name="Elixir of the Mongoose", sell_in=5, quality=7), 4),
            (Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80), 80),
            (Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80), 80),
            (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20), 23),
            (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49), 50),
            (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49), 50),
            (Item(name="Conjured Mana Cake", sell_in=3, quality=6), 3),  # <-- :O
        ],
    )
    def test_updates_item_quality_three_times(self, item: Item, quantity: int) -> None:
        items = [item]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()

        expect(quantity).to(equal(items[0].quality))

    @pytest.mark.parametrize(
        "item,quantity",
        [
            (Item(name="+5 Dexterity Vest", sell_in=10, quality=20), 16),
            (Item(name="Aged Brie", sell_in=2, quality=0), 6),
            (Item(name="Elixir of the Mongoose", sell_in=5, quality=7), 3),
            (Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80), 80),
            (Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80), 80),
            (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20), 24),
            (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49), 50),
            (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49), 50),
            (Item(name="Conjured Mana Cake", sell_in=3, quality=6), 1),  # <-- :O
        ],
    )
    def test_updates_item_quality_four_times(self, item: Item, quantity: int) -> None:
        items = [item]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()

        expect(quantity).to(equal(items[0].quality))

    @pytest.mark.parametrize(
        "item,quantity",
        [
            (Item(name="+5 Dexterity Vest", sell_in=10, quality=20), 14),
            (Item(name="Aged Brie", sell_in=2, quality=0), 10),
            (Item(name="Elixir of the Mongoose", sell_in=5, quality=7), 0),
            (Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80), 80),
            (Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80), 80),
            (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20), 27),
            (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49), 50),
            (Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49), 0),
            (Item(name="Conjured Mana Cake", sell_in=3, quality=6), 0),  # <-- :O
        ],
    )
    def test_updates_item_quality_six_times(self, item: Item, quantity: int) -> None:
        items = [item]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()

        expect(quantity).to(equal(items[0].quality))
