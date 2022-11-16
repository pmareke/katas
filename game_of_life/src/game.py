from dataclasses import dataclass

from game_of_life.src.board import Board


@dataclass
class Game:
    board: Board


class GameFactory:
    @staticmethod
    def make(board: Board) -> Game:
        return Game(board=board)
