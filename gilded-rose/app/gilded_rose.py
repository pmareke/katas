from typing import List

from app.domain.item import Item


class GildedRose:
    def __init__(self, items: List[Item]):
        self.items = items

    def update_quality(self) -> None:
        [item.update() for item in self.items]
