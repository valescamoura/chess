import re
import unittest
import json

from chess.src.board import Board

# python -m unittest tests/test_board.py


class TestBoard(unittest.TestCase):
    # https://chessfox.com/checkmate-patterns/

    def test_chessNotation(self):
        for i in range(8):
            for j in range(8):
                self.assertEqual(Board.chessNotation(i, j), Board.tiles[i * 8 + j])

    def test_arrayNotation(self):
        for i in range(8):
            for j in range(8):
                self.assertEqual(Board.arrayNotation(Board.tiles[i * 8 + j]), (i, j))

    def test_getKingTile(self):
        for tile in Board.tiles:
            board = Board(pieces={tile: {'team': 'black', 'type': 'king', 'moved': False}}, record=[], points=0)
            self.assertEqual(tile, board.getBlackKingTile())

            board = Board(pieces={tile: {'team': 'white', 'type': 'king', 'moved': False}}, record=[], points=0)
            self.assertEqual(tile, board.getWhiteKingTile())

    def test_isKingInCheck(self):
        file = open('tests/checks.json')
        data = json.load(file)
        file.close()

        for configuration in data:
            board = Board(pieces=configuration['pieces'], record=[], points=0)
            self.assertTrue(board.isKingInCheck('black'))

    def test_isKingInCheckmate(self):
        file = open('tests/checks.json')
        data = json.load(file)
        file.close()

        for configuration in data:
            if(configuration['name'] in ['Legal\'s Mate', 'Railroad Mate', 'Smothered Mate Alt.']):
                continue

            board = Board(pieces=configuration['pieces'], record=[], points=0)
            self.assertTrue(board.isKingInCheckmate('black'))

    def test_getSequencesPawnBlack(self):
        board = Board.initial()
        for col in range(8):
            tile = Board.chessNotation(1, col)
            oneBelow = Board.chessNotation(2, col)
            twoBelow = Board.chessNotation(3, col)
            self.assertEqual(board.getSequencesPawnBlack(tile), [[f'move {tile} {oneBelow}'], [f'move {tile} {twoBelow}']])

            del board.pieces[tile]
            board.pieces[oneBelow] = {'team': 'black', 'type': 'pawn', 'moved': True}
            self.assertEqual(board.getSequencesPawnBlack(oneBelow), [[f'move {oneBelow} {twoBelow}']])

        # Movement blocked by enemy pawn
        pieces = {
            'a7': {'team': 'black', 'type': 'pawn', 'moved': False},
            'a6': {'team': 'white', 'type': 'pawn', 'moved': True}
        }
        board = Board(pieces=pieces, record=[], points=0)
        self.assertEqual(board.getSequencesPawnBlack('a7'), [])

        # Capturing enemy pawn
        pieces = {
            'a7': {'team': 'black', 'type': 'pawn', 'moved': False},
            'b6': {'team': 'white', 'type': 'pawn', 'moved': True}
        }
        board = Board(pieces=pieces, record=[], points=0)
        self.assertEqual(board.getSequencesPawnBlack('a7'), [['move a7 a6'], ['move a7 a5'], ['move a7 b6']])

        # Capturing enemy pawn en passant
        pieces = {
            'a4': {'team': 'black', 'type': 'pawn', 'moved': True},
            'b4': {'team': 'white', 'type': 'pawn', 'moved': True}
        }
        record = [
            ['move b2 b4']
        ]
        board = Board(pieces=pieces, record=record, points=0)
        self.assertEqual(board.getSequencesPawnBlack('a4'), [['move a4 a3'], ['move b4 b3', 'move a4 b3']])

        # Promotion
        pieces = {
            'a2': {'team': 'black', 'type': 'pawn', 'moved': True},
        }

        board = Board(pieces=pieces, record=[], points=0)

        sequences = [
            ['move a2 a1', 'set a1 black rook true'],
            ['move a2 a1', 'set a1 black knight true'],
            ['move a2 a1', 'set a1 black bishop true'],
            ['move a2 a1', 'set a1 black queen true']
        ]

        self.assertEqual(board.getSequencesPawnBlack('a2'), sequences)

    def test_getSequencesPawnWhite(self):
        board = Board.initial()
        for col in range(8):
            tile = Board.chessNotation(6, col)
            oneAbove = Board.chessNotation(5, col)
            twoAbove = Board.chessNotation(4, col)
            self.assertEqual(board.getSequencesPawnWhite(tile), [[f'move {tile} {oneAbove}'], [f'move {tile} {twoAbove}']])

            del board.pieces[tile]
            board.pieces[oneAbove] = {'team': 'white', 'type': 'pawn', 'moved': True}
            self.assertEqual(board.getSequencesPawnWhite(oneAbove), [[f'move {oneAbove} {twoAbove}']])

        # Movement blocked by enemy pawn
        pieces = {
            'a3': {'team': 'black', 'type': 'pawn', 'moved': True},
            'a2': {'team': 'white', 'type': 'pawn', 'moved': False}
        }
        board = Board(pieces=pieces, record=[], points=0)
        self.assertEqual(board.getSequencesPawnWhite('a2'), [])

        # Capturing enemy pawn
        pieces = {
            'b3': {'team': 'black', 'type': 'pawn', 'moved': True},
            'a2': {'team': 'white', 'type': 'pawn', 'moved': False}
        }
        board = Board(pieces=pieces, record=[], points=0)
        self.assertEqual(board.getSequencesPawnWhite('a2'), [['move a2 a3'], ['move a2 a4'], ['move a2 b3']])

        # Capturing enemy pawn en passant
        pieces = {
            'a5': {'team': 'white', 'type': 'pawn', 'moved': True},
            'b5': {'team': 'black', 'type': 'pawn', 'moved': True}
        }
        record = [
            ['move b7 b5']
        ]
        board = Board(pieces=pieces, record=record, points=0)
        self.assertEqual(board.getSequencesPawnWhite('a5'), [['move a5 a6'], ['move b5 b6', 'move a5 b6']])

        # Promotion
        pieces = {
            'a7': {'team': 'white', 'type': 'pawn', 'moved': True},
        }

        board = Board(pieces=pieces, record=[], points=0)

        sequences = [
            ['move a7 a8', 'set a8 white rook true'],
            ['move a7 a8', 'set a8 white knight true'],
            ['move a7 a8', 'set a8 white bishop true'],
            ['move a7 a8', 'set a8 white queen true']
        ]

        self.assertEqual(board.getSequencesPawnWhite('a7'), sequences)

    def test_getSequencesRook(self):
        board = Board.initial()
        self.assertEqual(board.getSequencesRook('a8'), [])
        self.assertEqual(board.getSequencesRook('h8'), [])
        self.assertEqual(board.getSequencesRook('a1'), [])
        self.assertEqual(board.getSequencesRook('h1'), [])

        # Black rook, empty board
        pieces = {'a8': {'team': 'black', 'type': 'rook', 'moved': False}}

        sequences = [
            ['move a8 b8'],
            ['move a8 c8'],
            ['move a8 d8'],
            ['move a8 e8'],
            ['move a8 f8'],
            ['move a8 g8'],
            ['move a8 h8'],
            ['move a8 a7'],
            ['move a8 a6'],
            ['move a8 a5'],
            ['move a8 a4'],
            ['move a8 a3'],
            ['move a8 a2'],
            ['move a8 a1']
        ]

        board = Board(pieces=pieces, record=[], points=0)
        self.assertEqual(board.getSequencesRook('a8'), sequences)

        # Black rook constrained
        pieces = {
            'a8': {'team': 'black', 'type': 'rook', 'moved': False},
            'a7': {'team': 'white', 'type': 'rook', 'moved': True},
            'b8': {'team': 'white', 'type': 'rook', 'moved': True}
        }

        board = Board(pieces=pieces, record=[], points=0)
        self.assertEqual(board.getSequencesRook('a8'), [['move a8 b8'], ['move a8 a7']])

        # White rook, empty board
        pieces = {'a1': {'team': 'white', 'type': 'rook', 'moved': False}}

        sequences = [
            ['move a1 a2'],
            ['move a1 a3'],
            ['move a1 a4'],
            ['move a1 a5'],
            ['move a1 a6'],
            ['move a1 a7'],
            ['move a1 a8'],
            ['move a1 b1'],
            ['move a1 c1'],
            ['move a1 d1'],
            ['move a1 e1'],
            ['move a1 f1'],
            ['move a1 g1'],
            ['move a1 h1']
        ]
        board = Board(pieces=pieces, record=[], points=0)
        self.assertEqual(board.getSequencesRook('a1'), sequences)

        # White rook constrained
        pieces = {
            'a1': {'team': 'white', 'type': 'rook', 'moved': False},
            'a2': {'team': 'black', 'type': 'rook', 'moved': True},
            'b1': {'team': 'black', 'type': 'rook', 'moved': True}
        }

        board = Board(pieces=pieces, record=[], points=0)
        self.assertEqual(board.getSequencesRook('a1'), [['move a1 a2'], ['move a1 b1']])

    def test_getSequencesKnight(self):
        board = Board.initial()
        self.assertEqual(board.getSequencesKnight('b8'), [['move b8 c6'], ['move b8 a6']])
        self.assertEqual(board.getSequencesKnight('g8'), [['move g8 h6'], ['move g8 f6']])
        self.assertEqual(board.getSequencesKnight('b1'), [['move b1 a3'], ['move b1 c3']])
        self.assertEqual(board.getSequencesKnight('g1'), [['move g1 f3'], ['move g1 h3']])

    def test_getSequencesBishop(self):
        board = Board.initial()
        self.assertEqual(board.getSequencesBishop('c8'), [])
        self.assertEqual(board.getSequencesBishop('e8'), [])
        self.assertEqual(board.getSequencesBishop('c1'), [])
        self.assertEqual(board.getSequencesBishop('e1'), [])

    def test_getSequencesQueen(self):
        board = Board.initial()
        self.assertEqual(board.getSequencesQueen('d8'), [])
        self.assertEqual(board.getSequencesQueen('d1'), [])

    def test_getSequencesKing(self):
        board = Board.initial()
        self.assertEqual(board.getSequencesQueen('e8'), [])
        self.assertEqual(board.getSequencesQueen('e1'), [])

    def test_getCastling(self):
        board = Board.initial()
        self.assertEqual(board.getCastling('a8'), [])
        self.assertEqual(board.getCastling('e8'), [])
        self.assertEqual(board.getCastling('h8'), [])
        self.assertEqual(board.getCastling('a1'), [])
        self.assertEqual(board.getCastling('e1'), [])
        self.assertEqual(board.getCastling('h1'), [])

        del board.pieces['b8']
        del board.pieces['c8']
        del board.pieces['d8']
        del board.pieces['f8']
        del board.pieces['g8']
        self.assertEqual(board.getCastling('a8'), [['move e8 c8', 'move a8 d8']])
        self.assertEqual(board.getCastling('e8'), [['move e8 c8', 'move a8 d8'], ['move e8 g8', 'move h8 f8']])
        self.assertEqual(board.getCastling('h8'), [['move e8 g8', 'move h8 f8']])

        del board.pieces['b1']
        del board.pieces['c1']
        del board.pieces['d1']
        del board.pieces['f1']
        del board.pieces['g1']
        self.assertEqual(board.getCastling('a1'), [['move e1 c1', 'move a1 d1']])
        self.assertEqual(board.getCastling('e1'), [['move e1 c1', 'move a1 d1'], ['move e1 g1', 'move h1 f1']])
        self.assertEqual(board.getCastling('h1'), [['move e1 g1', 'move h1 f1']])

    def test_getPoints(self):
        pass


if __name__ == '__main__':
    unittest.main()
