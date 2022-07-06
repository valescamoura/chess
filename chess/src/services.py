from chess.src.board import *
from chess.src.ia import *


class Services:

    def __init__(self):
        self.chess = Board.initial()
        self.moves = 0

        self.queen = 2
        self.rook = 4
        self.knight = 4
        self.bishop = 4
        self.pawn = 16

    # create the new game and return the dictionary
    def start_game(self):
        self.chess = Board.initial()
        self.moves = 0

        self.queen = 2
        self.rook = 4
        self.knight = 4
        self.bishop = 4
        self.pawn = 16
        return self.chess.pieces

    def set_board(self, pieces, points, record):
        self.chess.pieces = pieces
        self.chess.points = int(points)
        self.chess.record = record

    def get_board(self):
        return self.chess.pieces, self.chess.points, self.chess.record

    # receive a string and will return a list of string with the possible moves
    def get_legal_moves(self, piece):
        sequences = self.chess.getLegalSequences(piece)
        result = []
        for i in range(len(sequences)):
            sequences[i] = sequences[i][0].split(" ")
            result.append(sequences[i][2])

        return result

    # receive a string to represent the piece and another to represent where it should go
    # output is the new dictionary
    def execute_move(self, piece, final, newType):
        print(type(piece), type(final))
        print(type(self.chess.points))
        move = "move " + piece + " " + final
        print(move)
        sequences = self.chess.getLegalSequences(piece)
        executed = False

        promotion = False

        queen = 0
        knight = 0
        rook = 0
        bishop = 0
        pawn = 0

        if self.chess.pieces[piece]["team"] == "white":
            if final[1] == "8":
                if self.chess.pieces[piece]["type"] == "pawn":
                    promotion = True

            for i in range(len(sequences)):
                if len(sequences[i]) > 1:
                    if move == sequences[i][1]:
                        for j in range(len(sequences[i])):
                            self.chess.execute(sequences[i][j])
                            executed = True
                            self.moves = 0
                if move == sequences[i][0]:
                    if promotion:
                        if newType == sequences[i][1].split()[3]:
                            for j in range(len(sequences[i])):
                                quant = len(self.chess.pieces)
                                self.chess.execute(sequences[i][j])
                                executed = True
                                if self.chess.pieces[final]["type"] == "pawn" or quant != len(self.chess.pieces):
                                    self.moves = 0
                                else:
                                    self.moves += 1
                            if executed:
                                break

                    else:
                        for j in range(len(sequences[i])):
                            quant = len(self.chess.pieces)
                            self.chess.execute(sequences[i][j])
                            executed = True
                            if self.chess.pieces[final]["type"] == "pawn" or quant != len(self.chess.pieces):
                                self.moves = 0
                            else:
                                self.moves += 1
                        if executed:
                            break

            for i in self.chess.pieces:
                if self.chess.pieces[i]["type"] == "knight":
                    knight += 1
                if self.chess.pieces[i]["type"] == "bishop":
                    bishop += 1
                if self.chess.pieces[i]["type"] == "rook":
                    rook += 1
                if self.chess.pieces[i]["type"] == "queen":
                    queen += 1
                if self.chess.pieces[i]["type"] == "pawn":
                    pawn += 1

            self.queen = queen
            self.rook = rook
            self.knight = knight
            self.bishop = bishop
            self.pawn = pawn

        return self.chess.pieces

    # IA movement
    # output is the new dictionary
    def IAMove_medio(self):
        sequence = alpha_beta(self.chess)
        if sequence:
            self.chess.execute(sequence)

        queen = 0
        knight = 0
        rook = 0
        bishop = 0
        pawn = 0

        for i in self.chess.pieces:
            if self.chess.pieces[i]["type"] == "knight":
                knight += 1
            if self.chess.pieces[i]["type"] == "bishop":
                bishop += 1
            if self.chess.pieces[i]["type"] == "rook":
                rook += 1
            if self.chess.pieces[i]["type"] == "queen":
                queen += 1
            if self.chess.pieces[i]["type"] == "pawn":
                pawn += 1

        self.queen = queen
        self.rook = rook
        self.knight = knight
        self.bishop = bishop
        self.pawn = pawn
        return self.chess.pieces

    def IAMove_facil(self, team = 'black'):
        sequence = rand(self.chess, team)
        if sequence:
            self.chess.execute(sequence)

        queen = 0
        knight = 0
        rook = 0
        bishop = 0
        pawn = 0

        for i in self.chess.pieces:
            if self.chess.pieces[i]["type"] == "knight":
                knight += 1
            if self.chess.pieces[i]["type"] == "bishop":
                bishop += 1
            if self.chess.pieces[i]["type"] == "rook":
                rook += 1
            if self.chess.pieces[i]["type"] == "queen":
                queen += 1
            if self.chess.pieces[i]["type"] == "pawn":
                pawn += 1

        self.queen = queen
        self.rook = rook
        self.knight = knight
        self.bishop = bishop
        self.pawn = pawn
        return self.chess.pieces

    # receive the team and return true if there is a possible move for the team
    def legalSequences(self, team):
        movements = []
        possible = False
        for piece in self.chess.pieces:
            if self.chess.pieces[piece]['team'] == team:
                movements.append(self.chess.getLegalSequences(piece))
                if len(movements[-1]) > 0:
                    possible = True

        if possible:
            return True
        else:
            return False

    def drawn(self):
        # Afogamento
        if not Services.legalSequences(self, "white"):
            if not self.chess.isKingInCheck("white"):
                return True

        if not Services.legalSequences(self, "black"):
            if not self.chess.isKingInCheck("black"):
                return True

        # regra dos 50 lances
        if self.moves >= 50:
            return True

        # peças insuficientes
        if self.pawn == 0:
            if self.queen == 0:
                if self.rook == 0:
                    if self.bishop == 1 and self.knight == 0:
                        return True
                    if self.knight == 1 and self.bishop == 0:
                        return True
                    if self.knight == 0 and self.bishop == 0:
                        return True

        return False

    def didPlayerWin(self):
        return self.chess.isKingInCheckmate("black")

    def didIAWin(self):
        return self.chess.isKingInCheckmate("white")
