from chess.src.board import *
from chess.src.ia import *


class Services:

    def __init__(self):
        self.chess = Board.initial()

    # create the new game and return the dictionary
    def start_game(self):
        self.chess = Board.initial()
        return self.chess.pieces

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
    def execute_move(self, piece, final):
        move = "move " + piece + " " + final
        sequences = self.chess.getLegalSequences(piece)
        executed = False
        newType = ""
        promotion = False

        if self.chess.pieces[piece]["team"] == "white":
            if final[1] == "8":
                if self.chess.pieces[piece]["type"] == "pawn":
                    newType = input()
                    promotion = True

            for i in range(len(sequences)):
                if move == sequences[i][0]:
                    if promotion:
                        if newType == sequences[i][1].split()[3]:
                            for j in range(len(sequences[i])):
                                self.chess.execute(sequences[i][j])
                                executed = True
                            if executed:
                                break

                    else:
                        for j in range(len(sequences[i])):
                            self.chess.execute(sequences[i][j])
                            executed = True
                        if executed:
                            break

        return self.chess.pieces

    # IA movement
    # output is the new dictionary
    def IAMove_medio(self):
        sequence = alpha_beta(self.chess)
        if sequence:
            self.chess.execute(sequence)
        return self.chess.pieces #tabuleiro

    def IAMove_facil(self):
        sequence = rand(self.chess)
        if sequence:
            self.chess.execute(sequence)
        return self.chess.pieces #tabuleiro

    # receive the team and return true if there is a possible move for the team
    def legalSequences(self, team):
        movements = []
        for piece in self.chess.pieces:
            if self.chess.pieces[piece]['team'] == team:
                movements.append(self.chess.getLegalSequences(piece))

        if movements:
            return True
        else:
            return False

    def drawn(self):
        if not Services.legalSequences(self, "white"):
            if not self.chess.isKingInCheck("white"):
                return True

        if not Services.legalSequences(self, "black"):
            if not self.chess.isKingInCheck("black"):
                return True

        return False

    def didPlayerWin(self):
        return self.chess.isKingInCheckmate("black")

    def didIAWin(self):
        return self.chess.isKingInCheckmate("white")
