import pytest

from expects import expect, equal
from app.gilded_rose import GildedRose
from app.domain.item import Item


class TestGildedRose:
    def test_updates_items(self) -> None:
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        expect("foo").to(equal(items[0].name))
