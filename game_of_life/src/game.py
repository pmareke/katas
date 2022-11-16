from dataclasses import dataclass

from game_of_life.src.board import Board


@dataclass
class Game:
    board: Board

    def next(self) -> None:
        self.board.update()


class GameFactory:
    @staticmethod
    def make(board: Board) -> Game:
        return Game(board=board)
