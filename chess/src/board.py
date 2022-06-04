from multipledispatch import dispatch
import copy
import json


class Board:
    '''
    Chess board implementation.
    Keeps a record of all changes to the board, but not of whose turn to play it is (therefore does not detect stalemates reliably).
    '''

    types = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
    '''
    Names of pieces in a game of chess.
    '''

    teams = ['black', 'white']
    '''
    Names of teams in a game of chess.
    '''

    ranks = ['8', '7', '6', '5', '4', '3', '2', '1']
    '''Chess notation ranks (board "rows").'''

    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    '''Chess notation files (board "columns").'''

    tiles = [
        'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
        'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
        'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
        'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
        'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
        'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
        'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
        'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'
    ]
    '''Ordered pairs of file and rank (board "squares").'''

    def __init__(self, pieces, record, points):
        self.pieces = pieces
        self.record = record
        self.points = points

    def initial():
        pieces = {
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
            'a2': {'team': 'white', 'type': 'pawn',   'moved': False},
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
        }

        record = []
        points = 0

        return Board(pieces=pieces, record=record, points=points)

    def toJson(self, indent=None, separators=(',', ':')):
        dictionary = {'pieces': self.pieces, 'record': self.record}
        return json.dumps(dictionary, indent=indent, separators=separators)

    def fromJson(string):
        dictionary = json.loads(dictionary)
        return Board(pieces=dictionary['pieces'], record=dictionary['record'])

    def copy(self):
        return copy.copy(self)

    def deepcopy(self):
        return copy.deepcopy(self)

    def toString(self):
        output = '  ' + ''.join(Board.files) + '\n'

        for rank in range(8, 0, -1):

            output += f'{rank} '
            for file in Board.files:
                tile = f'{file}{rank}'

                character = ' '
                piece = self.pieces.get(tile, None)
                if piece is not None:
                    character = piece['type'][0]
                    if piece['team'] == 'black':
                        character = character.lower()
                    else:
                        character = character.upper()

                output += character

            output += f' {rank}\n'

        output += '  ' + ''.join(Board.files)

        return output

    @dispatch(str, int, int)
    def chessNotation(tile: str, dy: int, dx: int):
        '''
        Returns <tile> in chess notation, offset by <dy> rows and <dx> cols in array notation.

        example:

        chessNotation('a8', 1,  1) -> 'b7'

        chessNotation('a8', 0, -1) -> None
        '''
        row, col = Board.arrayNotation(tile)
        if row is not None and col is not None:
            return Board.chessNotation(row + dy, col + dx)

        return None

    @dispatch(int, int)
    def chessNotation(row: int, col: int):
        '''
        Returns a string containing rank and file, in chess notation, equivalent to <row> and <col>, in array notation.

        example:

        chessNotation(0,  0) -> 'a8'

        chessNotation(0, -1) -> None, None
        '''
        if -1 < row < len(Board.ranks) and -1 < col < len(Board.files):
            return f'{Board.files[col]}{Board.ranks[row]}'

        return None

    def arrayNotation(tile: str):
        '''
        Returns a tuple of row and col, in array notation, equivalent to rank and file of <tile>, in chess notation.

        example:

        arrayNotation('a1') -> 7, 0

        arrayNotation('z9') -> None
        '''
        file = tile[0]
        rank = tile[1]
        if file in Board.files and rank in Board.ranks:
            return Board.ranks.index(rank), Board.files.index(file)

        return None, None

    @dispatch(list)
    def execute(self, sequence: list, record=True):
        '''
        Executes a sequence of commands. Performs rollback if an exception gets thrown.

        del <tile>

        set <tile> <team> <type> <moved>

        move <src> <dst>

        swap <src> <dst>
        '''
        backup = self.deepcopy()
        try:
            for command in sequence:
                self.execute(command, record=False)

            if record:
                self.record.append(sequence)

        except Exception as e:
            self = backup

    @dispatch(str)
    def execute(self, command: str, record=True):
        '''
        Executes a command. Performs rollback if an exception gets thrown.

        del <tile>

        set <tile> <team> <type> <moved>

        move <src> <dst>

        swap <src> <dst>
        '''
        backup = self.deepcopy()
        scores = {'pawn': 10, 'rook': 50, 'knight': 30, 'bishop': 30, 'queen': 90, 'king': 900}

        try:
            if 'del' in command:
                _, tile = command.split(' ')

                if tile not in Board.tiles:
                    raise Exception(f'Invalid chess tile: "{tile}"')

                if tile in self.pieces:
                    # A piece gets deleted
                    if self.pieces[tile]['team'] == 'black':
                        self.points -= scores[self.pieces[tile]['type']]
                    else:
                        self.points += scores[self.pieces[tile]['type']]

                    del self.pieces[tile]

            elif 'set' in command:
                _, tile, team, type, moved = command.split(' ')

                if tile not in Board.tiles:
                    raise Exception(f'Invalid chess tile: "{tile}"')

                if team not in Board.teams:
                    raise Exception(f'Invalid chess team: "{team}"')

                if type not in Board.types:
                    raise Exception(f'Invalid piece type: "{type}"')

                if tile in self.pieces:
                    # A piece gets overwritten
                    if self.pieces[tile]['team'] == 'black':
                        self.points -= scores[self.pieces[tile]['type']]
                    else:
                        self.points += scores[self.pieces[tile]['type']]

                self.pieces[tile] = {'team': team, 'type': type, 'moved': (moved.lower() == 'true')}
                if self.pieces[tile]['team'] == 'black':
                    self.points += scores[self.pieces[tile]['type']]
                else:
                    self.points -= scores[self.pieces[tile]['type']]

            elif 'move' in command:
                _, src, dst = command.split(' ')

                if src not in Board.tiles:
                    raise Exception(f'Invalid chess tile: "{src}"')

                if dst not in Board.tiles:
                    raise Exception(f'Invalid chess tile: "{dst}"')

                if src in self.pieces:
                    if dst in self.pieces:
                        # A piece gets overwritten
                        if self.pieces[dst]['team'] == 'black':
                            self.points -= scores[self.pieces[dst]['type']]
                        else:
                            self.points += scores[self.pieces[dst]['type']]

                    self.pieces[dst] = self.pieces[src]
                    self.pieces[dst]['moved'] = True
                    del self.pieces[src]

            elif 'swap' in command:
                _, src, dst = command.split(' ')

                if src not in Board.tiles:
                    raise Exception(f'Invalid chess tile: "{src}"')

                if dst not in Board.tiles:
                    raise Exception(f'Invalid chess tile: "{dst}"')

                if src in self.pieces and dst in self.pieces:
                    aux = self.pieces[src]
                    self.pieces[src] = self.pieces[dst]
                    self.pieces[dst] = aux
                elif src in self.pieces:
                    self.pieces[dst] = self.pieces[src]
                    del self.pieces[src]
                elif dst in self.pieces:
                    self.pieces[src] = self.pieces[dst]
                    del self.pieces[dst]

            if record:
                self.record.append([command])

        except Exception as e:
            print(f'Failed to parse command: "{e}"')
            self = backup

    def getKingTile(self, team):
        '''
        Returns position of <team> king in chess notation. None if no <team> king in board.
        '''
        for tile in self.pieces:
            if self.pieces[tile]['type'] == 'king' and self.pieces[tile]['team'] == team:
                return tile
        return None

    def getBlackKingTile(self):
        '''
        Returns position of black king in chess notation.
        '''
        return self.getKingTile('black')

    def getWhiteKingTile(self):
        '''
        Returns position of white king in chess notation.
        '''
        return self.getKingTile('white')

    def isKingInCheck(self, team):
        '''
        Whether <team> king is in check.
        '''
        king = self.getKingTile(team)
        if not king:
            return False

        # Pawn
        if team == 'black':
            piece = self.pieces.get(Board.chessNotation(king, 1, -1), None)
            if piece and piece['team'] == 'white' and piece['type'] == 'pawn':
                return True

            piece = self.pieces.get(Board.chessNotation(king, 1,  1), None)
            if piece and piece['team'] == 'white' and piece['type'] == 'pawn':
                return True

        if team == 'white':
            piece = self.pieces.get(Board.chessNotation(king, -1, -1), None)
            if piece and piece['team'] == 'black' and piece['type'] == 'pawn':
                return True

            piece = self.pieces.get(Board.chessNotation(king, -1,  1), None)
            if piece and piece['team'] == 'black' and piece['type'] == 'pawn':
                return True

        # Straights: Rook or Queen
        # Left
        pieces = [piece for i in range(1, 8) if (piece == self.pieces.get(Board.chessNotation(king, 0, -i), None) is not None)]
        for piece in pieces:
            if piece['team'] != team and (piece['type'] == 'rook' or piece['type'] == 'queen'):
                return True
            break

        # Right
        pieces = [piece for i in range(1, 8) if (piece == self.pieces.get(Board.chessNotation(king, 0, i), None) is not None)]
        for piece in pieces:
            if piece['team'] != team and (piece['type'] == 'rook' or piece['type'] == 'queen'):
                return True
            break

        # Top
        pieces = [piece for i in range(1, 8) if (piece == self.pieces.get(Board.chessNotation(king, -i, 0), None) is not None)]
        for piece in pieces:
            if piece['team'] != team and (piece['type'] == 'rook' or piece['type'] == 'queen'):
                return True
            break

        # Bottom
        pieces = [piece for i in range(1, 8) if (piece == self.pieces.get(Board.chessNotation(king, i, 0), None) is not None)]
        for piece in pieces:
            if piece['team'] != team and (piece['type'] == 'rook' or piece['type'] == 'queen'):
                return True
            break

        # Diagonals: Bishop or Queen
        # Top left
        pieces = [piece for i in range(1, 8) if (piece == self.pieces.get(Board.chessNotation(king, -i, -i), None) is not None)]
        for piece in pieces:
            if piece['team'] != team and (piece['type'] == 'bishop' or piece['type'] == 'queen'):
                return True
            break

        # Top right
        pieces = [piece for i in range(1, 8) if (piece == self.pieces.get(Board.chessNotation(king, -i, i), None) is not None)]
        for piece in pieces:
            if piece['team'] != team and (piece['type'] == 'bishop' or piece['type'] == 'queen'):
                return True
            break

        # Bottom right
        pieces = [piece for i in range(1, 8) if (piece == self.pieces.get(Board.chessNotation(king,  i, i), None) is not None)]
        for piece in pieces:
            if piece['team'] != team and (piece['type'] == 'bishop' or piece['type'] == 'queen'):
                return True
            break

        # Bottom left
        pieces = [piece for i in range(1, 8) if (piece == self.pieces.get(Board.chessNotation(king,  i, -i), None) is not None)]
        for piece in pieces:
            if piece['team'] != team and (piece['type'] == 'bishop' or piece['type'] == 'queen'):
                return True
            break

        # Knights
        deltas = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
        pieces = [piece for delta in deltas if (piece == self.pieces.get(Board.chessNotation(king, delta[0], delta[1]), None) is not None)]
        for piece in pieces:
            if piece['team'] != team and piece['type'] == 'knight':
                return True

        # Kings
        deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        pieces = [piece for delta in deltas if (piece == self.pieces.get(Board.chessNotation(king, delta[0], delta[1]), None) is not None)]
        for piece in pieces:
            if piece['team'] != team and piece['type'] == 'king':
                return True

        return False

    def isBlackKingInCheck(self):
        '''
        Whether black king is in check.
        '''
        return self.isKingInCheck('black')

    def isWhiteKingInCheck(self):
        '''
        Whether white king is in check.
        '''
        return self.isKingInCheck('white')

    def isKingInCheckmate(self, team: str):
        '''
        Whether king of <team> team is in checkmate.
        '''
        king = self.getKingTile(team)
        if king and self.isKingInCheck(team) and len(self.getLegalSequences(king)) == 0:
            return True

        return False

    def isBlackKingInCheckmate(self):
        '''
        Whether black king is in checkmate.
        '''
        return self.isKingInCheckmate('black')

    def isWhiteKingInCheckmate(self):
        '''
        Whether white king is in checkmate.
        '''
        return self.isKingInCheckmate('white')

    def getLegalSequences(self, tile: str, testCastling=True, testPromotion=True, testEnPassant=True):
        '''
        Returns a list of sequences of moves avaiable for piece in <tile>, without leaving the respective king in check.
        '''
        piece = self.pieces.get(tile, None)
        if piece is None:
            return []

        sequences = []
        for sequence in self.getSequences(tile, testCastling=testCastling, testPromotion=testPromotion, testEnPassant=testEnPassant):
            clone = self.deepcopy()
            clone.execute(sequence)
            if not clone.isKingInCheck(piece['team']):
                sequences.append(sequence)
        return sequences

    def getSequences(self, tile: str, testCastling=True, testPromotion=True, testEnPassant=True):
        '''
        Returns a list of sequences of moves avaiable for piece in <tile>, but does not check if they would leave it's king in check.
        '''
        piece = self.pieces.get(tile, None)
        if piece is None:
            return []

        if piece['type'] == 'pawn':
            if piece['team'] == 'black':
                return self.getSequencesPawnBlack(tile)

            elif piece['team'] == 'white':
                return self.getSequencesPawnWhite(tile)

        elif piece['type'] == 'rook':
            return self.getSequencesRook(tile)

        elif piece['type'] == 'knight':
            return self.getSequencesKnight(tile)

        elif piece['type'] == 'bishop':
            return self.getSequencesBishop(tile)

        elif piece['type'] == 'queen':
            return self.getSequencesQueen(tile)

        elif piece['type'] == 'king':
            return self.getSequencesKing(tile)

        return []

    def getSequencesPawnBlack(self, tile, testPromotion=True, testEnPassant=True):
        piece = self.pieces.get(tile, None)
        if piece is None:
            return []

        if piece['type'] != 'pawn' or piece['team'] != 'black':
            return []

        sequences = []

        oneBelow = Board.chessNotation(tile, 1, 0)
        twoBelow = Board.chessNotation(tile, 2, 0)

        if oneBelow is not None and self.pieces.get(oneBelow, None) is None:
            # Regular move
            sequences.append([f'move {tile} {oneBelow}'])

            if twoBelow is not None and self.pieces.get(twoBelow, None) is None and not piece['moved']:
                # Optional first move
                sequences.append([f'move {tile} {twoBelow}'])

        for delta in [(1, -1), (1, 1)]:
            otherTile = Board.chessNotation(tile, delta[0], delta[1])
            if otherTile is not None:
                otherPiece = self.pieces.get(otherTile, None)
                if otherPiece is not None:
                    if otherPiece['team'] == 'white':
                        # Regular attack
                        sequences.append([f'move {tile} {otherTile}'])
                else:
                    if testEnPassant:
                        aboveOtherTile = Board.chessNotation(otherTile, -1, 0)
                        belowOtherTile = Board.chessNotation(otherTile,  1, 0)
                        if belowOtherTile is not None and self.pieces.get(aboveOtherTile, None) == {'team': 'white', 'type': 'pawn', 'moved': True}:
                            if len(self.record) > 0 and len(self.record[-1]) > 0 and self.record[-1][-1] == f'move {belowOtherTile} {aboveOtherTile}':
                                # En passant
                                sequences.append([f'move {aboveOtherTile} {otherTile}', f'move {tile} {otherTile}'])

        if testPromotion:
            new_sequences = []
            for sequence in sequences:
                _, src, dst = sequence[-1].split(' ')
                if src == tile and dst[1] == '1':
                    # Sequence results in pawn across the board
                    new_sequences.append(sequence + [f'set {dst} black rook true'])
                    new_sequences.append(sequence + [f'set {dst} black knight true'])
                    new_sequences.append(sequence + [f'set {dst} black bishop true'])
                    new_sequences.append(sequence + [f'set {dst} black queen true'])
                else:
                    # Sequence does not result in pawn across the board
                    new_sequences.append(sequence)
            return new_sequences

        return sequences

    def getSequencesPawnWhite(self, tile, testPromotion=True, testEnPassant=True):
        piece = self.pieces.get(tile, None)
        if piece is None:
            return []

        if piece['type'] != 'pawn' or piece['team'] != 'white':
            return []

        sequences = []

        oneAbove = Board.chessNotation(tile, -1, 0)
        twoAbove = Board.chessNotation(tile, -2, 0)

        if oneAbove is not None and self.pieces.get(oneAbove, None) is None:
            # Regular move
            sequences.append([f'move {tile} {oneAbove}'])

            if twoAbove is not None and self.pieces.get(twoAbove, None) is None and not piece['moved']:
                # Optional first move
                sequences.append([f'move {tile} {twoAbove}'])

        for delta in [(-1, -1), (-1, 1)]:
            otherTile = Board.chessNotation(tile, delta[0], delta[1])
            if otherTile is not None:
                otherPiece = self.pieces.get(otherTile, None)
                if otherPiece is not None:
                    if otherPiece['team'] == 'black':
                        # Regular attack
                        sequences.append([f'move {tile} {otherTile}'])
                else:
                    if testEnPassant:
                        aboveOtherTile = Board.chessNotation(otherTile, -1, 0)
                        belowOtherTile = Board.chessNotation(otherTile,  1, 0)
                        if aboveOtherTile is not None and self.pieces.get(belowOtherTile) == {'team': 'black', 'type': 'pawn', 'moved': True}:
                            if len(self.record) > 0 and len(self.record[-1]) > 0 and self.record[-1][-1] == f'move {aboveOtherTile} {belowOtherTile}':
                                # En passant
                                sequences.append([f'move {belowOtherTile} {otherTile}', f'move {tile} {otherTile}'])

        if testPromotion:
            new_sequences = []
            for sequence in sequences:
                _, src, dst = sequence[-1].split(' ')
                if src == tile and dst[1] == '1':
                    # Sequence results in pawn across the board
                    new_sequences.append(sequence + [f'set {dst} white rook true'])
                    new_sequences.append(sequence + [f'set {dst} white knight true'])
                    new_sequences.append(sequence + [f'set {dst} white bishop true'])
                    new_sequences.append(sequence + [f'set {dst} white queen true'])
                else:
                    # Sequence does not result in pawn across the board
                    new_sequences.append(sequence)
            return new_sequences

        return sequences

    def getSequencesRook(self, tile, testCastling=True):
        piece = self.pieces.get(tile, None)
        if piece is None:
            return []

        if piece['type'] != 'rook':
            return []

        sequences = []

        deltas = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        for delta in deltas:
            i = 1
            otherTile = Board.chessNotation(tile, i * delta[0], i * delta[1])
            while otherTile is not None:
                i += 1
                otherPiece = self.pieces.get(otherTile, None)
                if otherPiece is None:
                    sequences.append([f'move {tile} {otherTile}'])
                else:
                    if otherPiece['team'] != piece['team']:
                        sequences.append([f'move {tile} {otherTile}'])
                    break
                otherTile = Board.chessNotation(tile, i * delta[0], i * delta[1])

        if testCastling:
            sequences += self.getCastling(tile)

        return sequences

    def getSequencesKnight(self, tile):
        piece = self.pieces.get(tile, None)
        if piece is None:
            return []

        if piece['type'] != 'knight':
            return []

        sequences = []

        deltas = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

        for delta in deltas:
            otherTile = Board.chessNotation(tile, delta[0], delta[1])
            if otherTile is not None:
                otherPiece = self.pieces.get(otherTile, None)
                if otherPiece is None or otherPiece['team'] != piece['team']:
                    sequences.append([f'move {tile} {otherTile}'])

        return sequences

    def getSequencesBishop(self, tile):
        piece = self.pieces.get(tile, None)
        if piece is None:
            return []

        if piece['type'] != 'bishop':
            return []

        sequences = []

        deltas = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for delta in deltas:
            i = 1
            otherTile = Board.chessNotation(tile, i * delta[0], i * delta[1])
            while otherTile is not None:
                i += 1
                otherPiece = self.pieces.get(otherTile, None)
                if otherPiece is None:
                    sequences.append([f'move {tile} {otherTile}'])
                else:
                    if otherPiece['team'] != piece['team']:
                        sequences.append([f'move {tile} {otherTile}'])
                    break
                otherTile = Board.chessNotation(tile, i * delta[0], i * delta[1])

        return sequences

    def getSequencesQueen(self, tile):
        piece = self.pieces.get(tile, None)
        if piece is None:
            return []

        if piece['type'] != 'queen':
            return []

        sequences = []

        deltas = [(-1, -1), (-1, 1), (1, -1), (1, 1)] + [(0, -1), (-1, 0), (0, 1), (1, 0)]

        for delta in deltas:
            i = 1
            otherTile = Board.chessNotation(tile, i * delta[0], i * delta[1])
            while otherTile is not None:
                i += 1
                otherPiece = self.pieces.get(otherTile, None)
                if otherPiece is None:
                    sequences.append([f'move {tile} {otherTile}'])
                else:
                    if otherPiece['team'] != piece['team']:
                        sequences.append([f'move {tile} {otherTile}'])
                    break
                otherTile = Board.chessNotation(tile, i * delta[0], i * delta[1])

        return sequences

    def getSequencesKing(self, tile, testCastling=True):
        piece = self.pieces.get(tile, None)
        if piece is None:
            return []

        if piece['type'] != 'king':
            return []

        sequences = []

        deltas = [(-1, -1), (-1, 1), (1, -1), (1, 1)] + [(0, -1), (-1, 0), (0, 1), (1, 0)]

        for delta in deltas:
            otherTile = Board.chessNotation(tile, delta[0], delta[1])
            if otherTile is not None:
                otherPiece = self.pieces.get(otherTile, None)
                if otherPiece is None or otherPiece['team'] != piece['team']:
                    sequences.append([f'move {tile} {otherTile}'])

        if testCastling:
            sequences += self.getCastling(tile)

        return sequences

    def getCastling(self, tile):
        '''
        Returns a list of sequences of castling moves avaiable for piece in <tile>. Pointless if piece is not a king or rook.
        '''

        blackKingIsInCheck = None
        whiteKingIsInCheck = None

        sequences = []

        if tile == 'a8' or tile == 'e8':
            if self.pieces.get('a8', None) == {'team': 'black', 'type': 'rook', 'moved': False}:
                if self.pieces.get('e8', None) == {'team': 'black', 'type': 'king', 'moved': False}:
                    if self.pieces.get('c8', None) is None:
                        if self.pieces.get('d8', None) is None:
                            if blackKingIsInCheck is None:
                                blackKingIsInCheck = self.isKingInCheck('black')
                            if not blackKingIsInCheck:
                                sequences.append(['move e8 c8', 'move a8 d8'])

        if tile == 'h8' or tile == 'e8':
            if self.pieces.get('h8', None) == {'team': 'black', 'type': 'rook', 'moved': False}:
                if self.pieces.get('e8', None) == {'team': 'black', 'type': 'king', 'moved': False}:
                    if self.pieces.get('g8', None) is None:
                        if self.pieces.get('f8', None) is None:
                            if blackKingIsInCheck is None:
                                blackKingIsInCheck = self.isKingInCheck('black')
                            if not blackKingIsInCheck:
                                sequences.append(['move e8 g8', 'move h8 f8'])

        if tile == 'a1' or tile == 'e1':
            if self.pieces.get('a1', None) == {'team': 'white', 'type': 'rook', 'moved': False}:
                if self.pieces.get('e1', None) == {'team': 'white', 'type': 'king', 'moved': False}:
                    if self.pieces.get('c1', None) is None:
                        if self.pieces.get('d1', None) is None:
                            if whiteKingIsInCheck is None:
                                whiteKingIsInCheck = self.isKingInCheck('white')
                            if not whiteKingIsInCheck:
                                sequences.append(['move e1 c1', 'move a1 d1'])

        if tile == 'h1' or tile == 'e1':
            if self.pieces.get('h1', None) == {'team': 'white', 'type': 'rook', 'moved': False}:
                if self.pieces.get('e1', None) == {'team': 'white', 'type': 'king', 'moved': False}:
                    if self.pieces.get('g1', None) is None:
                        if self.pieces.get('f1', None) is None:
                            if whiteKingIsInCheck is None:
                                whiteKingIsInCheck = self.isKingInCheck('white')
                            if not whiteKingIsInCheck:
                                sequences.append(['move e1 g1', 'move h1 f1'])

        return sequences
