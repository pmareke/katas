from typing import List
from expects import expect, be_none

from game_of_life.src.board import Board
from game_of_life.src.cell import Cell, DeadCell
from game_of_life.src.game import GameFactory


class TestGame:
    def test_creates_a_game(self) -> None:
        cells: List[List[Cell]] = [
            [DeadCell(), DeadCell(),
             DeadCell(), DeadCell()],
            [DeadCell(), DeadCell(),
             DeadCell(), DeadCell()],
            [DeadCell(), DeadCell(),
             DeadCell(), DeadCell()],
        ]
        board = Board(cells)
        game = GameFactory.make(board)

        expect(game).not_to(be_none)
