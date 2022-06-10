from chess.src.board import *
from chess.src.ia import *

global chess

class Services:

    # create the new game and return the dictionary
    def start_game():
        global chess
        chess = Board.initial()
        return chess.pieces

    # receive a string and will return a list of string with the possible moves
    def get_legal_moves(piece):
        global chess
        sequences = chess.getLegalSequences(piece)
        result = []
        for i in range(len(sequences)):
            sequences[i] = sequences[i][0].split(" ")
            result.append(sequences[i][2])

        return result

    # receive a string to represent the piece and another to represent where it should go
    # output is the new dictionary
    def execute_move(piece, final): # APAGAR: ids
        global chess
        move = "move " + piece + " " + final
        sequences = chess.getLegalSequences(piece)
        executed = False
        newType = ""
        promotion = False
        if final[1] == "8":
            if chess.pieces[piece]["type"] == "pawn" and chess.pieces[piece]["team"] == "white":
                newType = input()
                promotion = True

        for i in range(len(sequences)):

            if promotion:
                if move == sequences[i][0]:
                    if newType == sequences[i][1].split()[3]:
                        for j in range(len(sequences[i])):
                            chess.execute(sequences[i][j])
                            executed = True
                        if executed:
                            break

            else:
                for j in range(len(sequences[i])):
                    chess.execute(sequences[i][j])
                    executed = True
                if executed:
                    break

        return chess.pieces

    # IA movement
    # output is the new dictionary
    def IAMove():
        sequence = alpha_beta(chess)
        if sequence:
            chess.execute(sequence)
        return chess.pieces #tabuleiro

    # receive the team and return true if there is a possible move for the team
    def legalSequences(team):
        global chess
        movements = []
        for piece in chess.pieces:
            if chess.pieces[piece]['team'] == team:
                movements.append(chess.getLegalSequences(piece))

        if movements:
            return True
        else:
            return False

    def drawn():
        global chess
        if not Services.legalSequences("white"):
            if not chess.isKingInCheckmate("white"):
                return True

        if not Services.legalSequences("black"):
            if not chess.isKingInCheckmate("black"):
                return True

        return False

    def didPlayerWin():
        global chess
        return chess.isKingInCheckmate("black")

    def didIAWin():
        global chess
        return chess.isKingInCheckmate("white")


