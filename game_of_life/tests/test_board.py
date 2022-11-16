from typing import List
from expects import be_within, expect, have_length

from game_of_life.src.board import Board, BoardFactory
from game_of_life.src.cell import Cell, DeadCell


class TestBoard:
    def test_creates_a_random_board(self) -> None:
        board = BoardFactory.make()

        expect(board.cells).to(have_length(be_within(0, 11)))
        expect(board.cells[0]).to(have_length(be_within(0, 11)))

    def test_creates_a_custom_board(self) -> None:
        cells: List[List[Cell]] = [[DeadCell()]]
        board = Board(cells)

        expect(board.cells).to(have_length(1))
        expect(board.cells[0]).to(have_length(1))
