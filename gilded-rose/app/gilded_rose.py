from typing import List

from app.domain.item import Item


class GildedRose:
    def __init__(self, items: List[Item]):
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            if item.name == "Aged Brie":
                self.aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.backstage(item)
            elif item.name != "Sulfuras, Hand of Ragnaros":
                self.normal_item(item)

    @staticmethod
    def normal_item(item):
        if item.quality > 0:
            item.quality = item.quality - 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.quality > 0:
                item.quality = item.quality - 1

    @staticmethod
    def backstage(item):
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.sell_in < 11:
                if item.quality < 50:
                    item.quality = item.quality + 1
            if item.sell_in < 6:
                if item.quality < 50:
                    item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = item.quality - item.quality

    @staticmethod
    def aged_brie(item):
        if item.quality < 50:
            item.quality = item.quality + 1
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.quality < 50:
                item.quality = item.quality + 1
