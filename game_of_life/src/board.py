import random
from dataclasses import dataclass
from typing import List

from game_of_life.src.cell import AliveCell, Cell, DeadCell


@dataclass
class Board:
    cells: List[List[Cell]]


class BoardFactory:
    @staticmethod
    def make() -> Board:
        rows = random.randint(1, 10)
        columns = random.randint(1, 10)
        cells: List[List[Cell]] = []
        for row in range(rows):
            cells.append([])
            for _ in range(columns):
                random_number = random.randint(1, 10)
                cell = AliveCell() if random_number % 2 == 0 else DeadCell()
                cells[row].append(cell)
        return Board(cells=cells)
