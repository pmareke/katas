from dataclasses import dataclass


@dataclass
class Cell:
    alive: bool


class AliveCell(Cell):
    def __init__(self) -> None:
        super().__init__(True)


class DeadCell(Cell):
    def __init__(self) -> None:
        super().__init__(False)
