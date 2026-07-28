from board import Board

board = Board(10,10)
print(board.get_vision())
print()
board.step((1,0), 10)
print(board.get_vision())