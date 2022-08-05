from dataclasses import dataclass
from typing import List

from app.domain.item import Item


@dataclass
class GildedRose:
    items: List[Item]

    def update_quality(self) -> None:
        for item in self.items:
            if item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.quality < 50:
                    self._item_quality_under_50(item)
            else:
                self._item_name_not_aged_brie_or_backstage(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                self._sell_in_under_0(item)

    @staticmethod
    def _item_quality_under_50(item: Item) -> None:
        item.quality = item.quality + 1
        if item.name == "Backstage passes to a TAFKAL80ETC concert" and item.sell_in < 11 and item.quality < 50:
            item.quality = item.quality + 1

    @staticmethod
    def _item_name_not_aged_brie_or_backstage(item: Item) -> None:
        if item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
            item.quality = item.quality - 1

    def _sell_in_under_0(self, item: Item) -> None:
        if item.name != "Aged Brie":
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.quality = item.quality - item.quality
            else:
                self._item_name_not_aged_brie_or_backstage(item)
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
