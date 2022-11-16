import random
from dataclasses import dataclass
from typing import List

from game_of_life.src.cell import AliveCell, Cell, DeadCell


@dataclass
class Board:
    cells: List[List[Cell]]

    def update(self) -> None:
        new_cells: List[List[Cell]] = []
        for row_index, _ in enumerate(self.cells):
            new_cells.append([])
            for column_index, _ in enumerate(self.cells[row_index]):
                new_cell = self._create_cell(row_index, column_index)
                new_cells[row_index].append(new_cell)
        self.cells = new_cells

    def _create_cell(self, row_index: int, column_index: int) -> Cell:
        cell = self.cells[row_index][column_index]
        live = 0
        for neighbord in self._neighbords(row_index, column_index):
            if neighbord.alive:
                live += 1
        if cell.alive and (live > 3 or live < 2):
            return DeadCell()
        if not cell.alive and live == 3:
            return AliveCell()
        return cell

    def _neighbords(self, row_index: int, column_index: int) -> List[Cell]:
        neighbords: List[Cell] = []
        if row_index - 1 >= 0:
            neighbords.append(self.cells[row_index - 1][column_index])
        if column_index - 1 >= 0:
            neighbords.append(self.cells[row_index][column_index - 1])
        if row_index - 1 >= 0 and column_index - 1 >= 0:
            neighbords.append(self.cells[row_index - 1][column_index - 1])
        if row_index + 1 < len(self.cells):
            neighbords.append(self.cells[row_index + 1][column_index])
        if column_index + 1 < len(self.cells[row_index]):
            neighbords.append(self.cells[row_index][column_index + 1])
        if row_index + 1 < len(self.cells) and column_index + 1 < len(
            self.cells[row_index]
        ):
            neighbords.append(self.cells[row_index + 1][column_index + 1])
        return neighbords


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
