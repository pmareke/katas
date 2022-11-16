from dataclasses import dataclass


@dataclass
class Cell:
    alive: bool


class AliveCell:
    def __init__(self) -> None:
        self.cell = Cell(True)


class DeadCell:
    def __init__(self) -> None:
        self.cell = Cell(False)
