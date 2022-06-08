from board import *
from ia import *

chess = Board.initial()

black_can_move = True
white_can_move = True

command = ''
points = chess.points
winner = None
while not winner:
    try:
        print('\n' + chess.toString() + '\n')

        sequence = min_max(chess,"white")
        if sequence:
            white_can_move = True
            print(f'White Executing sequence: {sequence}')
            chess.execute(sequence)
        else:
            white_can_move = False

        if (points - chess.points) == 900 or chess.isBlackKingInCheckmate():
            winner = 'White' 
        points = chess.points
    
        sequence = alpha_beta(chess)
        if sequence:
            black_can_move = True
            print(f'Black Executing sequence: {sequence}')
            chess.execute(sequence)
        else:
            black_can_move = False

        if (chess.points - points) == 900 or chess.isWhiteKingInCheckmate():
            winner = 'Black' 
        points = chess.points


        print(f'Points: {chess.points}')
                

    except Exception as e:
        print(f'Exception thrown: {e}')

print('\n' + chess.toString() + '\n')
print(f'Game Over!\n{winner} won!!!')