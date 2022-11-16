from dataclasses import dataclass
from typing import List

from game_of_life.src.cell import Cell


@dataclass
class Board:
    rows: int
    columns: int

    def __post_init__(self) -> None:
        self.cells: List[List[Cell]] = []
        for row in range(self.rows):
            self.cells.append([])
            for _ in range(self.columns):
                self.cells[row].append(Cell())


class BoardFactory:
    @staticmethod
    def make(rows: int, columns: int) -> Board:
        return Board(rows=rows, columns=columns)
