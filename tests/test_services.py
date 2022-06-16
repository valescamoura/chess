import unittest
from chess.src.services import *

class TestService(unittest.TestCase):

    def test_start_game(self):
        self.assertEqual(Services.start_game(), {'a8': {'team': 'black', 'type': 'rook', 'moved': False}, 'b8': {'team': 'black', 'type': 'knight', 'moved': False}, 'c8': {'team': 'black', 'type': 'bishop', 'moved': False}, 'd8': {'team': 'black', 'type': 'queen', 'moved': False}, 'e8': {'team': 'black', 'type': 'king', 'moved': False}, 'f8': {'team': 'black', 'type': 'bishop', 'moved': False}, 'g8': {'team': 'black', 'type': 'knight', 'moved': False}, 'h8': {'team': 'black', 'type': 'rook', 'moved': False}, 'a7': {'team': 'black', 'type': 'pawn', 'moved': False}, 'b7': {'team': 'black', 'type': 'pawn', 'moved': False}, 'c7': {'team': 'black', 'type': 'pawn', 'moved': False}, 'd7': {'team': 'black', 'type': 'pawn', 'moved': False}, 'e7': {'team': 'black', 'type': 'pawn', 'moved': False}, 'f7': {'team': 'black', 'type': 'pawn', 'moved': False}, 'g7': {'team': 'black', 'type': 'pawn', 'moved': False}, 'h7': {'team': 'black', 'type': 'pawn', 'moved': False}, 'a2': {'team': 'white', 'type': 'pawn', 'moved': False}, 'b2': {'team': 'white', 'type': 'pawn', 'moved': False}, 'c2': {'team': 'white', 'type': 'pawn', 'moved': False}, 'd2': {'team': 'white', 'type': 'pawn', 'moved': False}, 'e2': {'team': 'white', 'type': 'pawn', 'moved': False}, 'f2': {'team': 'white', 'type': 'pawn', 'moved': False}, 'g2': {'team': 'white', 'type': 'pawn', 'moved': False}, 'h2': {'team': 'white', 'type': 'pawn', 'moved': False}, 'a1': {'team': 'white', 'type': 'rook', 'moved': False}, 'b1': {'team': 'white', 'type': 'knight', 'moved': False}, 'c1': {'team': 'white', 'type': 'bishop', 'moved': False}, 'd1': {'team': 'white', 'type': 'queen', 'moved': False}, 'e1': {'team': 'white', 'type': 'king', 'moved': False}, 'f1': {'team': 'white', 'type': 'bishop', 'moved': False}, 'g1': {'team': 'white', 'type': 'knight', 'moved': False}, 'h1': {'team': 'white', 'type': 'rook', 'moved': False}})

    #def test_get_legal_moves():
    #    pass
    
    #def test_execute_move():
    #    pass
    
    #def test_IAMove():
    #    pass

    #def test_legalSequences():
    #    pass

    #def test_didPlayerWin():
    #    pass
   
    #def test_didIAWin():
    #    pass

    #def test_drawn():
    #    pass 




if __name__ == '__main__':
    unittest.main()
   
