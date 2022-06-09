from board import *

pieces = {
    'e8': {'team': 'black', 'type': 'king', 'moved': False},
    'e1': {'team': 'white', 'type': 'king', 'moved': False},
    'a7': {'team': 'white', 'type': 'pawn', 'moved': True},
}

board = Board(pieces, [], 0)

print(board.toString())

print(board.getLegalSequences('a7'))
