from FileCom import *

y=FileCom()
board=y.read("easy1.txt")
board.displayBoard()
print(board.horizontal_validation(1,5))
print(board.vertical_validation(4,7))
print(board.block_validation(9,9,5))
