from app.domain.item import Item


class BackstageItem(Item):
    def __init__(self, sell_in: int, quality: int):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)

    def update(self) -> None:
        if self.quality < 50:
            self.quality = self.quality + 1
            if self.sell_in < 11 and self.quality < 50:
                self.quality = self.quality + 1
            if self.sell_in < 6 and self.quality < 50:
                self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = self.quality - self.quality
