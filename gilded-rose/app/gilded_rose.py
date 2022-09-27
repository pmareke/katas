from typing import List

from app.domain.item import Item


class GildedRose:

    @staticmethod
    def update_quality(items: List[Item]) -> None:
        for item in items:
            item.update()
