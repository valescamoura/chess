from board import *

pieces = {
    'a2': {'team': 'black', 'type': 'pawn', 'moved': True},
    'e8': {'team': 'black', 'type': 'king', 'moved': False},
    'e1': {'team': 'white', 'type': 'king', 'moved': False},
}

board = Board(pieces, [], 0)

print(board.toString())

print(board.getLegalSequences('a2'))
