from dataclasses import dataclass

from app.domain.item import Item


@dataclass(repr=False, eq=False)
class BackstageItem(Item):
    name = "Backstage passes to a TAFKAL80ETC concert"
    sell_in: int
    quality: int

    def update(self) -> None:
        if self.quality < 50:
            self.quality = self.quality + 1
            if self.sell_in < 11:
                if self.quality < 50:
                    self.quality = self.quality + 1
            if self.sell_in < 6:
                if self.quality < 50:
                    self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = self.quality - self.quality
