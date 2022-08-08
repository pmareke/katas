from dataclasses import dataclass

from app.domain.item import Item


@dataclass(repr=False, eq=False)
class SulfurasItem(Item):
    name: str
    sell_in: int
    quality: int

    def update(self) -> None:
        pass
