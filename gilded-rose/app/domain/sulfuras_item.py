from app.domain.item import Item


class SulfurasItem(Item):
    def __init__(self, sell_in: int, quality: int):
        super().__init__("Sulfuras, Hand of Ragnaros", sell_in, quality)

    def update(self) -> None:
        pass
