from chess import *

chess = Chess.initial()

command = ''
while command != 'exit':
    try:
        print('\n' + chess.toString() + '\n')
        print('Enter a command: ', end='')
        command = input()

        if 'reset' in command:
            chess = Chess.initial()

        elif 'sequences' in command:
            _, tile = command.split(' ')

            print(f'{tile}: {chess.getSequences(tile)}')

        elif 'execute' in command:

            sequence = [step.strip() for step in command.replace('execute', '').strip().split(',')]
            print(f'Executing sequence: {sequence}')
            chess.execute(sequence)

        elif 'pieces' in command:
            for tile in chess.pieces:
                piece = chess.pieces[tile]
                print(f'{tile}: ({piece["team"]} {(piece["type"] + ",").ljust(7)} moved={piece["moved"]})')

        elif 'record' in command:
            for sequence in chess.record:
                print(sequence)


    except Exception as e:
        print(f'Exception thrown: {e}')
