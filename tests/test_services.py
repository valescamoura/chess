import unittest
from chess.src.services import Services
from chess.src.board import Board
from unittest.mock import patch


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

        # tabuleiro inicial
        teste = Services()
        with patch.object(Board, 'getLegalSequences', return_value=[['move a2 a3'], ['move a2 a4']]):
            assert teste.get_legal_moves("a2") == ["a3", "a4"]

        with patch.object(Board, 'getLegalSequences', return_value=[['move a7 a6'], ['move a7 a5']]):
            assert teste.get_legal_moves("a7") == ["a6", "a5"]

        with patch.object(Board, 'getLegalSequences', return_value=[]):
            assert teste.get_legal_moves("a1") == []

        with patch.object(Board, 'getLegalSequences', return_value=[['move b1 a3'], ['move b1 c3']]):
            assert teste.get_legal_moves("b1") == ["a3", "c3"]

        with patch.object(Board, 'getLegalSequences', return_value=[]):
            assert teste.get_legal_moves("c1") == []

        with patch.object(Board, 'getLegalSequences', return_value=[]):
            assert teste.get_legal_moves("d1") == []

        with patch.object(Board, 'getLegalSequences', return_value=[]):
            assert teste.get_legal_moves("e1") == []

        with patch.object(Board, 'getLegalSequences', return_value=[]):
            assert teste.get_legal_moves("f1") == []

        with patch.object(Board, 'getLegalSequences', return_value=[['move g1 f3'], ['move g1 h3']]):
            assert teste.get_legal_moves("g1") == ["f3", "h3"]

        with patch.object(Board, 'getLegalSequences', return_value=[]):
            assert teste.get_legal_moves("h1") == []

        with patch.object(Board, 'getLegalSequences', return_value=[]):
            assert teste.get_legal_moves("a8") == []

        with patch.object(Board, 'getLegalSequences', return_value=[['move b8 c6'], ['move b8 a6']]):
            assert teste.get_legal_moves("b8") == ["c6", "a6"]

        with patch.object(Board, 'getLegalSequences', return_value=[]):
            assert teste.get_legal_moves("c8") == []

        with patch.object(Board, 'getLegalSequences', return_value=[]):
            assert teste.get_legal_moves("e8") == []

        with patch.object(Board, 'getLegalSequences', return_value=[]):
            assert teste.get_legal_moves("f8") == []

        with patch.object(Board, 'getLegalSequences', return_value=[['move g8 h6'], ['move g8 f6']]):
            assert teste.get_legal_moves("g8") == ["h6", "f6"]

        with patch.object(Board, 'getLegalSequences', return_value=[]):
            assert teste.get_legal_moves("h8") == []

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
        with patch.object(Board, 'getLegalSequences', return_value=[['move b8 c7'], ['move b8 c8'], ['move b8 b7']]):
            assert teste.get_legal_moves("b8") == ["c7", "c8", "b7"]

        with patch.object(Board, 'getLegalSequences', return_value=[['move e1 d2'], ['move e1 f2'], ['move e1 e2'], ['move e1 f1'], ['move e1 g1', 'move h1 f1']]):
            assert teste.get_legal_moves("e1") == ["d2", "f2", "e2", "f1", "g1"]

        with patch.object(Board, 'getLegalSequences', return_value=[['move h1 g1'], ['move h1 f1'], ['move h1 h2'], ['move h1 h3'], ['move h1 h4'], ['move h1 h5'], ['move h1 h6'], ['move h1 h7'], ['move h1 h8'], ['move e1 g1', 'move h1 f1']]):
            assert teste.get_legal_moves("h1") == ['g1', 'f1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'g1']

        # roque maior rei branco
        teste.chess.pieces = {
            'a1': {'team': 'white', 'type': 'rook', 'moved': False},
            'e1': {'team': 'white', 'type': 'king', 'moved': False},
            'f1': {'team': 'white', 'type': 'knight', 'moved': False},
            'g1': {'team': 'white', 'type': 'bishop', 'moved': False},
            'h1': {'team': 'white', 'type': 'rook', 'moved': False},
            "b8": {'team': 'black', 'type': 'king', 'moved': False}
        }

        with patch.object(Board, 'getLegalSequences', return_value=[['move a1 a2'], ['move a1 a3'], ['move a1 a4'], ['move a1 a5'], ['move a1 a6'], ['move a1 a7'], ['move a1 a8'], ['move a1 b1'], ['move a1 c1'], ['move a1 d1'], ['move e1 c1', 'move a1 d1']]):
            assert teste.get_legal_moves("a1") == ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'c1', 'd1', 'c1']

        with patch.object(Board, 'getLegalSequences', return_value=[['move e1 d2'], ['move e1 f2'], ['move e1 d1'], ['move e1 e2'], ['move e1 c1', 'move a1 d1']]):
            assert teste.get_legal_moves("h8") == ['d2', 'f2', 'd1', 'e2', 'c1']

        # en passant
        teste.chess.pieces = {
            'a1': {'team': 'black', 'type': 'king', 'moved': False},
            'e1': {'team': 'white', 'type': 'king', 'moved': False},
            'd5': {'team': 'white', 'type': 'pawn', 'moved': True},
            'e5': {'team': 'black', 'type': 'pawn', 'moved': True}
        }
        teste.chess.record = [["move d4 d5"], ["move e7 e5"]]
        with patch.object(Board, 'getLegalSequences', return_value=[['move d5 d6'], ['move e5 e6', 'move d5 e6']]):
            assert teste.get_legal_moves("d5") == ['d6', 'e6']

        teste.chess.pieces = {
            'a1': {'team': 'black', 'type': 'king', 'moved': False},
            'e1': {'team': 'white', 'type': 'king', 'moved': False},
            'd5': {'team': 'white', 'type': 'pawn', 'moved': True},
            'c5': {'team': 'black', 'type': 'pawn', 'moved': True}
        }
        teste.chess.record = [['move d4 d5'], ['move c7 c5']]
        with patch.object(Board, 'getLegalSequences', return_value=[['move d5 d6'], ['move c5 c6', 'move d5 e6']]):
            assert teste.get_legal_moves("d5") == ['d6', 'c6']

        # check mate, peças pretas sem movimentação possível
        teste.start_game()
        teste.chess.pieces = {
            'a1': {'team': 'white', 'type': 'king', 'moved': False},
            'e1': {'team': 'black', 'type': 'king', 'moved': False},
            'a3': {'team': 'black', 'type': 'rook', 'moved': True},
            'b3': {'team': 'black', 'type': 'rook', 'moved': True},
            'f1': {'team': 'white', 'type': 'rook', 'moved': True}
        }
        with patch.object(Board, 'getLegalSequences', return_value=[]):
            assert teste.get_legal_moves("a1") == []
        with patch.object(Board, 'getLegalSequences', return_value=[]):
            assert teste.get_legal_moves("f1") == []

        # promoção de peão
        teste.chess.pieces = {
            'a1': {'team': 'white', 'type': 'king', 'moved': False},
            'e1': {'team': 'black', 'type': 'king', 'moved': False},
            'b7': {'team': 'white', 'type': 'pawn', 'moved': True}
        }
        with patch.object(Board, 'getLegalSequences', return_value=[['move b7 b8', 'set b8 white rook true'], ['move b7 b8', 'set b8 white knight true'], ['move b7 b8', 'set b8 white bishop true'], ['move b7 b8', 'set b8 white queen true']]):
            assert teste.get_legal_moves("b7") == ['b8', 'b8', 'b8', 'b8']

        # movimentação com check
        teste.chess.pieces = {
            'a1': {'team': 'white', 'type': 'rook', 'moved': False},
            'b1': {'team': 'white', 'type': 'rook', 'moved': True},
            'e1': {'team': 'white', 'type': 'king', 'moved': False},
            'h7': {'team': 'black', 'type': 'rook', 'moved': False},
            "b8": {'team': 'black', 'type': 'king', 'moved': True}
        }

        with patch.object(Board, 'getLegalSequences', return_value=[["move h7 c7"], ["move h7 c8"]]):
            assert teste.get_legal_moves("b8") == ['c7', 'c8']

        with patch.object(Board, 'getLegalSequences', return_value=[["move c7 b7"]]):
            assert teste.get_legal_moves("c7") == ['b7']
    
    def test_execute_move(self):
        teste = Services()
        self.assertEqual(teste.execute_move("a2", "a4", ""), {
            'a8': {'team': 'black', 'type': 'rook',   'moved': False},
            'b8': {'team': 'black', 'type': 'knight', 'moved': False},
            'c8': {'team': 'black', 'type': 'bishop', 'moved': False},
            'd8': {'team': 'black', 'type': 'queen',  'moved': False},
            'e8': {'team': 'black', 'type': 'king',   'moved': False},
            'f8': {'team': 'black', 'type': 'bishop', 'moved': False},
            'g8': {'team': 'black', 'type': 'knight', 'moved': False},
            'h8': {'team': 'black', 'type': 'rook',   'moved': False},
            #
            'a7': {'team': 'black', 'type': 'pawn',   'moved': False},
            'b7': {'team': 'black', 'type': 'pawn',   'moved': False},
            'c7': {'team': 'black', 'type': 'pawn',   'moved': False},
            'd7': {'team': 'black', 'type': 'pawn',   'moved': False},
            'e7': {'team': 'black', 'type': 'pawn',   'moved': False},
            'f7': {'team': 'black', 'type': 'pawn',   'moved': False},
            'g7': {'team': 'black', 'type': 'pawn',   'moved': False},
            'h7': {'team': 'black', 'type': 'pawn',   'moved': False},
            #
            'a4': {'team': 'white', 'type': 'pawn',   'moved': True},
            'b2': {'team': 'white', 'type': 'pawn',   'moved': False},
            'c2': {'team': 'white', 'type': 'pawn',   'moved': False},
            'd2': {'team': 'white', 'type': 'pawn',   'moved': False},
            'e2': {'team': 'white', 'type': 'pawn',   'moved': False},
            'f2': {'team': 'white', 'type': 'pawn',   'moved': False},
            'g2': {'team': 'white', 'type': 'pawn',   'moved': False},
            'h2': {'team': 'white', 'type': 'pawn',   'moved': False},
            #
            'a1': {'team': 'white', 'type': 'rook',   'moved': False},
            'b1': {'team': 'white', 'type': 'knight', 'moved': False},
            'c1': {'team': 'white', 'type': 'bishop', 'moved': False},
            'd1': {'team': 'white', 'type': 'queen',  'moved': False},
            'e1': {'team': 'white', 'type': 'king',   'moved': False},
            'f1': {'team': 'white', 'type': 'bishop', 'moved': False},
            'g1': {'team': 'white', 'type': 'knight', 'moved': False},
            'h1': {'team': 'white', 'type': 'rook',   'moved': False},
        })

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

        with patch.object(Board, 'getLegalSequences',
                          return_value=[['move e1 d2'], ['move e1 f2'], ['move e1 e2'], ['move e1 f1'],
                                        ['move e1 g1', 'move h1 f1']]):
            assert teste.execute_move("e1", "g1", "") == {
                'a1': {'team': 'white', 'type': 'rook', 'moved': False},
                'b1': {'team': 'white', 'type': 'knight', 'moved': False},
                'c1': {'team': 'white', 'type': 'bishop', 'moved': False},
                'd1': {'team': 'white', 'type': 'queen', 'moved': False},
                'g1': {'team': 'white', 'type': 'king', 'moved': True},
                'f1': {'team': 'white', 'type': 'rook', 'moved': True},
                "b8": {'team': 'black', 'type': 'king', 'moved': False}
            }

        # en passant
        teste.chess.pieces = {
                'a1': {'team': 'black', 'type': 'king', 'moved': False},
                'e1': {'team': 'white', 'type': 'king', 'moved': False},
                'd5': {'team': 'white', 'type': 'pawn', 'moved': True},
                'e5': {'team': 'black', 'type': 'pawn', 'moved': True}
        }
        teste.chess.record = [["move d4 d5"], ["move e7 e5"]]
        with patch.object(Board, 'getLegalSequences', return_value=[['move d5 d6'], ['move e5 e6', 'move d5 e6']]):
            assert teste.execute_move("d5", "e6", "") == {
                'a1': {'team': 'black', 'type': 'king', 'moved': False},
                'e1': {'team': 'white', 'type': 'king', 'moved': False},
                'e6': {'team': 'white', 'type': 'pawn', 'moved': True}
        }

        # promoção de peão
        teste.chess.pieces = {
                'a1': {'team': 'white', 'type': 'king', 'moved': False},
                'e1': {'team': 'black', 'type': 'king', 'moved': False},
                'b7': {'team': 'white', 'type': 'pawn', 'moved': True}
            }
        with patch.object(Board, 'getLegalSequences', return_value=[['move b7 b8', 'set b8 white rook true'],
                                                                        ['move b7 b8', 'set b8 white knight true'],
                                                                        ['move b7 b8', 'set b8 white bishop true'],
                                                                        ['move b7 b8', 'set b8 white queen true']]):
            assert teste.execute_move("b7", "b8", "queen") == {
                    'a1': {'team': 'white', 'type': 'king', 'moved': False},
                    'e1': {'team': 'black', 'type': 'king', 'moved': False},
                    'b8': {'team': 'white', 'type': 'queen', 'moved': True}
                }

    def test_legalSequences(self):
        teste = Services()

        teste.start_game()
        self.assertTrue(teste.legalSequences("white"))
        self.assertTrue(teste.legalSequences("black"))

        # rei preto sem movimentação pela rainha branca, logo time preto sem movimentação
        teste.chess.pieces = {
                              'a8': {'team': 'black', 'type': 'king',   'moved': True},
                              'c7': {'team': 'white', 'type': 'queen',   'moved': True},
                              'c4': {'team': 'white', 'type': 'king',   'moved': True}
                              }
        self.assertFalse(teste.legalSequences("black"))
        self.assertTrue(teste.legalSequences("white"))

        # rei branco sem movimentação pela rainha preta, logo time branco sem movimentação
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
   
