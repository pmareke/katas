from dataclasses import dataclass
from typing import List

from app.domain.item import Item


@dataclass
class GildedRose:
    items: List[Item]

    def update_quality(self) -> None:
        for item in self.items:
            item.update()
