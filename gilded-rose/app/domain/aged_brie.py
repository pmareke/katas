from dataclasses import dataclass

from app.domain.item import Item


@dataclass(repr=False, eq=False)
class AgedBrieItem(Item):
    name: str
    sell_in: int
    quality: int

    def update(self) -> None:
        if self.quality < 50:
            self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.quality < 50:
                self.quality = self.quality + 1
