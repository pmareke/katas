from expects import expect, be_none

from game_of_life.src.board import BoardFactory
from game_of_life.src.game import GameFactory


class TestGame:
    def test_creates_a_game(self) -> None:
        board = BoardFactory.make(rows=4, columns=4)
        game = GameFactory.make(board)

        expect(game).not_to(be_none)
