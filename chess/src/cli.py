from board import *
from ia import *

chess = Board.initial()

command = ''
while command != 'exit':
    try:
        print('\n' + chess.toString() + '\n')
        print('Enter a command: ', end='')
        command = input()

        if 'reset' in command:
            chess = Board.initial()

        elif 'sequences' in command:
            _, tile = command.split(' ')

            print(f'{tile}: {chess.getSequences(tile)}')

        elif 'execute' in command:

            sequence = [step.strip() for step in command.replace('execute', '').strip().split(',')]
            print(f'Executing sequence: {sequence}')
            chess.execute(sequence)

            sequence = alpha_beta(chess)
            if sequence:
                print(f'Black Executing sequence: {sequence}')
                chess.execute(sequence)


        elif 'pieces' in command:
            for tile in chess.pieces:
                piece = chess.pieces[tile]
                print(f'{tile}: ({piece["team"]} {(piece["type"] + ",").ljust(7)} moved={piece["moved"]})')

        elif 'record' in command:
            for sequence in chess.record:
                print(sequence)

        elif 'points' in command:
            print(f'Points: {chess.points}')
                

    except Exception as e:
        print(f'Exception thrown: {e}')
