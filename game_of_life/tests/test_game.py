from typing import List
from expects import expect, be, be_none

from game_of_life.src.board import Board, BoardFactory
from game_of_life.src.cell import AliveCell, Cell, DeadCell
from game_of_life.src.game import GameFactory


class TestGame:
    def test_creates_a_game(self) -> None:
        board = BoardFactory.make()
        game = GameFactory.make(board)

        expect(game).not_to(be_none)

    def test_plays_a_move(self) -> None:
        cells: List[List[Cell]] = [[DeadCell()]]
        board = Board(cells)
        game = GameFactory.make(board)

        game.next()

        expect(type(cells[0][0])).to(be(DeadCell))

    def test_a_dead_cell_with_exactly_three_live_neighbours_will_come_to_life(
        self
    ) -> None:
        dead_cell = DeadCell()
        live_cell = AliveCell()
        cells: List[List[Cell]] = [
            [dead_cell, live_cell, dead_cell],
            [dead_cell, dead_cell, live_cell],
            [dead_cell, live_cell, dead_cell],
        ]
        board = Board(cells)
        game = GameFactory.make(board)

        game.next()

        expect(type(game.board.cells[1][1])).to(be(AliveCell))

    def test_a_live_cell_with_fewer_than_two_live_neighbours_dies(self) -> None:
        dead_cell = DeadCell()
        live_cell = AliveCell()
        cells: List[List[Cell]] = [
            [dead_cell, dead_cell, dead_cell],
            [dead_cell, live_cell, dead_cell],
            [dead_cell, dead_cell, dead_cell],
        ]
        board = Board(cells)
        game = GameFactory.make(board)

        game.next()

        expect(type(game.board.cells[1][1])).to(be(DeadCell))

    def test_a_live_cell_with_more_than_three_live_neighbours_dies(
        self
    ) -> None:
        live_cell = AliveCell()
        cells: List[List[Cell]] = [
            [live_cell, live_cell, live_cell],
            [live_cell, live_cell, live_cell],
            [live_cell, live_cell, live_cell],
        ]
        board = Board(cells)
        game = GameFactory.make(board)

        game.next()

        expect(type(game.board.cells[1][1])).to(be(DeadCell))

    def test_a_live_cell_with_two_or_three_live_neighbours_lives_unchanged(
        self
    ) -> None:
        dead_cell = DeadCell()
        live_cell = AliveCell()
        cells: List[List[Cell]] = [
            [dead_cell, dead_cell, live_cell],
            [dead_cell, live_cell, live_cell],
            [dead_cell, dead_cell, live_cell],
        ]
        board = Board(cells)
        game = GameFactory.make(board)

        game.next()

        expect(type(game.board.cells[1][1])).to(be(AliveCell))
