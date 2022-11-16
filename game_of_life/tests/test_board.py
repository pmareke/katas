from expects import expect, have_length
from game_of_life.src.board import BoardFactory


class TestBoard:
    def test_creates_a_board(self) -> None:
        board = BoardFactory.make(rows=3, columns=4)

        expect(board.cells).to(have_length(3))
