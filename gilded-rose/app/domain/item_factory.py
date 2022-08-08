from app.domain.aged_brie_item import AgedBrieItem
from app.domain.backstage_item import BackstageItem
from app.domain.item import Item
from app.domain.regular_item import RegularItem
from app.domain.sulfuras_item import SulfurasItem


class ItemFactory:
    @staticmethod
    def create_item(name: str, sell_in: int, quality: int) -> Item:
        if name == "Aged Brie":
            return AgedBrieItem(sell_in, quality)
        if name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstageItem(sell_in, quality)
        if name == "Sulfuras, Hand of Ragnaros":
            return SulfurasItem(sell_in, quality)
        return RegularItem(name, sell_in, quality)
