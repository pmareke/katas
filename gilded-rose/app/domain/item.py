from dataclasses import dataclass


@dataclass(repr=False, eq=False)
class Item:
    name: str
    sell_in: int
    quality: int

    def update(self) -> None:
        if self.quality > 0:
            self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.quality > 0:
                self.quality = self.quality - 1

    def __repr__(self) -> str:
        return f"{self.name}, {self.sell_in}, {self.quality}"
