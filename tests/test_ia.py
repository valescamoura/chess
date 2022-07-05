import unittest
from chess.src.ia import *
from chess.src.board import Board

class TestIA(unittest.TestCase):

    def test_rand(self):
        # test the random move generation
        board = Board.initial()

        # generates the movement
        move = rand(board,"white")
        piece = move[0].split()[1]
        piece_team = board.pieces[piece]["team"]

        self.assertEqual(piece_team, "white")

        # check if the movement is valid
        moved_piece = move[0].split()[2]
        legal_moves = [move[0].split()[2] for move in board.getLegalSequences(piece)]

        self.assertIn(moved_piece,legal_moves)


    def test_min_max(self):
        # test the min max algorithm with depth = 1 (returns the movement with the best score) 
        board = Board.initial()

        move = min_max(board,"white")
        move,points = move 

        piece = move[0].split()[1]
        piece_team = board.pieces[piece]["team"]

        self.assertEqual(piece_team, "white")
        
        # check if the movement is valid
        moved_piece = move[0].split()[2]
        legal_moves = [move[0].split()[2] for move in board.getLegalSequences(piece)]

        self.assertIn(moved_piece,legal_moves)

        # check if returns the best move
        board = Board.initial()
        board.pieces = {
            'e3': {'team': 'white', 'type': 'pawn',   'moved': True},
            'd4': {'team': 'black', 'type': 'bishop', 'moved': True},
            'f4': {'team': 'black', 'type': 'pawn',   'moved': True},

            'e8': {'team': 'black', 'type': 'king',   'moved': False},
            'e1': {'team': 'white', 'type': 'king',   'moved': False}
       }

        move = min_max(board,"white")
        move,points = move

        self.assertEqual(move[0][0],'move e3 d4')
        self.assertEqual(points,-330)

        # check if the points are correct
        board.execute(move)
        self.assertEqual(points,board.points)



    def test_in_min_max(self):
        # test the auxiliary function implementing the min max algorithm with alpha-beta prunning
        board = Board.initial()

        empty = in_min_max(board,0,-9999,9999)

        # check if the return when depth == 0
        self.assertEqual(empty, 0)

        board.pieces = {
            'f6': {'team': 'black', 'type': 'bishop', 'moved': True},
            'e5': {'team': 'white', 'type': 'knight', 'moved': True},
            'g5': {'team': 'white', 'type': 'pawn',   'moved': True},
            'c3': {'team': 'white', 'type': 'queen',  'moved': True},

            'e8': {'team': 'black', 'type': 'king',   'moved': False},
            'e1': {'team': 'white', 'type': 'king',   'moved': False}
       }

        points = in_min_max(board,2,-9999,9999)

        # check if the points are correct
        self.assertEqual(points, 95)

   
    def test_alpha_beta(self):
        # test the full implementation of the min max algorithm with alpha-beta prunning
        board = Board.initial()

        board.pieces = {
            'f6': {'team': 'black', 'type': 'bishop', 'moved': True},
            'e5': {'team': 'white', 'type': 'knight', 'moved': True},
            'g5': {'team': 'white', 'type': 'pawn',   'moved': True},
            'c3': {'team': 'white', 'type': 'queen',  'moved': True},

            'e8': {'team': 'black', 'type': 'king',   'moved': False},
            'e1': {'team': 'white', 'type': 'king',   'moved': False}
       }

        move = alpha_beta(board)[0]
        piece = move[0].split()[1]
        piece_team = board.pieces[piece]["team"]

        # check if it returns the best movement
        self.assertEqual(piece_team, "black")
        self.assertEqual(move[0],'move f6 g5')

        # check
        board.execute(move)
        self.assertEqual(board.points, 95)


if __name__ == '__main__':
    unittest.main()
   

