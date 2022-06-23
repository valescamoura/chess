import unittest
from chess.src.services import *


class TestService(unittest.TestCase):

    def test_start_game(self):
        teste = Services()
        # valores iniciais da classe

        teste.queen = 0
        teste.rook = 0
        teste.knight = 0
        teste.bishop = 0
        teste.pawn = 0

        self.assertEqual(teste.start_game(), {'a8': {'team': 'black', 'type': 'rook', 'moved': False}, 'b8': {'team': 'black', 'type': 'knight', 'moved': False}, 'c8': {'team': 'black', 'type': 'bishop', 'moved': False}, 'd8': {'team': 'black', 'type': 'queen', 'moved': False}, 'e8': {'team': 'black', 'type': 'king', 'moved': False}, 'f8': {'team': 'black', 'type': 'bishop', 'moved': False}, 'g8': {'team': 'black', 'type': 'knight', 'moved': False}, 'h8': {'team': 'black', 'type': 'rook', 'moved': False}, 'a7': {'team': 'black', 'type': 'pawn', 'moved': False}, 'b7': {'team': 'black', 'type': 'pawn', 'moved': False}, 'c7': {'team': 'black', 'type': 'pawn', 'moved': False}, 'd7': {'team': 'black', 'type': 'pawn', 'moved': False}, 'e7': {'team': 'black', 'type': 'pawn', 'moved': False}, 'f7': {'team': 'black', 'type': 'pawn', 'moved': False}, 'g7': {'team': 'black', 'type': 'pawn', 'moved': False}, 'h7': {'team': 'black', 'type': 'pawn', 'moved': False}, 'a2': {'team': 'white', 'type': 'pawn', 'moved': False}, 'b2': {'team': 'white', 'type': 'pawn', 'moved': False}, 'c2': {'team': 'white', 'type': 'pawn', 'moved': False}, 'd2': {'team': 'white', 'type': 'pawn', 'moved': False}, 'e2': {'team': 'white', 'type': 'pawn', 'moved': False}, 'f2': {'team': 'white', 'type': 'pawn', 'moved': False}, 'g2': {'team': 'white', 'type': 'pawn', 'moved': False}, 'h2': {'team': 'white', 'type': 'pawn', 'moved': False}, 'a1': {'team': 'white', 'type': 'rook', 'moved': False}, 'b1': {'team': 'white', 'type': 'knight', 'moved': False}, 'c1': {'team': 'white', 'type': 'bishop', 'moved': False}, 'd1': {'team': 'white', 'type': 'queen', 'moved': False}, 'e1': {'team': 'white', 'type': 'king', 'moved': False}, 'f1': {'team': 'white', 'type': 'bishop', 'moved': False}, 'g1': {'team': 'white', 'type': 'knight', 'moved': False}, 'h1': {'team': 'white', 'type': 'rook', 'moved': False}})
        self.assertEqual(teste.moves, 0)
        self.assertEqual(teste.queen, 2)
        self.assertEqual(teste.rook, 4)
        self.assertEqual(teste.knight, 4)
        self.assertEqual(teste.bishop, 4)
        self.assertEqual(teste.pawn, 16)

    def test_get_legal_moves(self):
        teste = Services()

        # tabuleiro inicial
        self.assertEqual(teste.get_legal_moves("a2"), ["a3", "a4"])
        self.assertEqual(teste.get_legal_moves("a7"), ["a6", "a5"])
        self.assertEqual(teste.get_legal_moves("a1"), [])
        self.assertEqual(teste.get_legal_moves("b1"), ["a3", "c3"])
        self.assertEqual(teste.get_legal_moves("c1"), [])
        self.assertEqual(teste.get_legal_moves("d1"), [])
        self.assertEqual(teste.get_legal_moves("e1"), [])
        self.assertEqual(teste.get_legal_moves("f1"), [])
        self.assertEqual(teste.get_legal_moves("g1"), ["f3", "h3"])
        self.assertEqual(teste.get_legal_moves("h1"), [])
        self.assertEqual(teste.get_legal_moves("a8"), [])
        self.assertEqual(teste.get_legal_moves("b8"), ["a6", "c6"])
        self.assertEqual(teste.get_legal_moves("c8"), [])
        self.assertEqual(teste.get_legal_moves("d8"), [])
        self.assertEqual(teste.get_legal_moves("e8"), [])
        self.assertEqual(teste.get_legal_moves("f8"), [])
        self.assertEqual(teste.get_legal_moves("g8"), ["f6", "h6"])
        self.assertEqual(teste.get_legal_moves("h8"), [])

        # roque menor rei branco
        teste.chess.pieces = {
            'a1': {'team': 'white', 'type': 'rook', 'moved': False},
            'b1': {'team': 'white', 'type': 'knight', 'moved': False},
            'c1': {'team': 'white', 'type': 'bishop', 'moved': False},
            'd1': {'team': 'white', 'type': 'queen', 'moved': False},
            'e1': {'team': 'white', 'type': 'king', 'moved': False},
            'h1': {'team': 'white', 'type': 'rook', 'moved': False},
            "b8": {'team': 'black', 'type': 'king', 'moved': False}
        }
        self.assertEqual(teste.get_legal_moves("b8"), ["b7", "c8", "c7"])
        self.assertEqual(teste.get_legal_moves("e1"), ["d2", "e2", "f1", "f2", "g1"])
        self.assertEqual(teste.get_legal_moves("h1"), ["h2", "h3", "h4", "h5", "h6", "h7", "h8", "f1", "g1"])

        # roque maior rei branco
        teste.chess.pieces = {
            'a1': {'team': 'white', 'type': 'rook', 'moved': False},
            'e1': {'team': 'white', 'type': 'king', 'moved': False},
            'f1': {'team': 'white', 'type': 'knight', 'moved': False},
            'g1': {'team': 'white', 'type': 'bishop', 'moved': False},
            'h1': {'team': 'white', 'type': 'rook', 'moved': False},
            "b8": {'team': 'black', 'type': 'king', 'moved': False}
        }
    
    #def test_execute_move():
    #    pass

    def test_legalSequences(self):
        teste = Services()

        teste.start_game()
        self.assertEqual(teste.legalSequences("white"), True)
        self.assertEqual(teste.legalSequences("black"), True)

        # rei preto sem movimentação pela rainha branca, logo time branco sem movimentação
        teste.chess.pieces = {
                              'a8': {'team': 'black', 'type': 'king',   'moved': True},
                              'c7': {'team': 'white', 'type': 'queen',   'moved': True},
                              'c4': {'team': 'white', 'type': 'king',   'moved': True}
                              }
        self.assertEqual(teste.legalSequences("black"), False)
        self.assertEqual(teste.legalSequences("white"), True)

        # rei branco sem movimentação pela rainha preta, logo time preto sem movimentação
        teste.chess.pieces = {
                              'a1': {'team': 'white', 'type': 'king',   'moved': True},
                              'c2': {'team': 'black', 'type': 'queen',   'moved': True},
                              'a8': {'team': 'black', 'type': 'king',   'moved': True}
                              }
        self.assertEqual(teste.legalSequences("black"), True)
        self.assertEqual(teste.legalSequences("white"), False)

    def test_drawn(self):
        teste = Services()

        # teste com tabuleiro inicial
        teste.start_game()
        self.assertEqual(teste.drawn(), False)

        # 50 movimentos
        teste.start_game()
        teste.moves = 50
        self.assertEqual(teste.drawn(), True)

        # peças insuficientes
        teste.start_game()
        teste.pawn = 0
        teste.queen = 0
        teste.rook = 0
        teste.knight = 1
        teste.bishop = 0
        self.assertEqual(teste.drawn(), True)

        teste.start_game()
        teste.pawn = 0
        teste.queen = 0
        teste.rook = 0
        teste.knight = 0
        teste.bishop = 1
        self.assertEqual(teste.drawn(), True)

        teste.start_game()
        teste.pawn = 0
        teste.queen = 0
        teste.rook = 0
        teste.knight = 0
        teste.bishop = 0
        self.assertEqual(teste.drawn(), True)

        # afogamento
        teste.start_game()
        teste.chess.pieces = {
                              'a8': {'team': 'black', 'type': 'king',   'moved': True},
                              'c7': {'team': 'white', 'type': 'queen',   'moved': True},
                              'c4': {'team': 'white', 'type': 'king',   'moved': True}
                              }
        self.assertEqual(teste.drawn(), True)

        teste.start_game()
        teste.chess.pieces = {
                              'h8': {'team': 'black', 'type': 'king',   'moved': True},
                              'g2': {'team': 'white', 'type': 'rook',   'moved': True},
                              'a7': {'team': 'white', 'type': 'rook', 'moved': True},
                              'c4': {'team': 'white', 'type': 'king',   'moved': True}
                              }
        self.assertEqual(teste.drawn(), True)

        teste.start_game()
        teste.chess.pieces = {
                              'a1': {'team': 'white', 'type': 'king',   'moved': True},
                              'c2': {'team': 'black', 'type': 'queen',   'moved': True},
                              'a8': {'team': 'black', 'type': 'king',   'moved': True}
                              }
        self.assertEqual(teste.drawn(), True)


if __name__ == '__main__':
    unittest.main()
   
