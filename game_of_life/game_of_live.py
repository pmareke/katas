from game_of_life.src.board import BoardFactory
from game_of_life.src.game import GameFactory

board = BoardFactory.make()
game = GameFactory.make(board)

TIMES = 0
while TIMES < 100:
    print(board)
    game.next()
    TIMES += 1
