from dataclasses import dataclass


@dataclass(repr=False, eq=False)
class Item:
    name: str
    sell_in: int
    quality: int

    def update(self) -> None:
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"{self.name}, {self.sell_in}, {self.quality}"
