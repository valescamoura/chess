from random import choice

def rand(chess_board):
  '''
    Choses a random move from a random black piece.
  '''

  black_pieces = []
  for tile in chess_board.pieces:
    if chess_board.pieces[tile]["team"] == "black":
      black_pieces.append(tile)


  moves = []
  while len(moves) == 0:
    tile = choice(black_pieces)

    moves = chess_board.getLegalSequences(tile)
  
  return choice(moves)

def min_max():
    """
        Tabela de valores de peças(baseado em sua equivalência com o peao):
            peao   : 10
            cavalo : 30
            bispo  : 30
            torre  : 50 
            rainha : 90
            rei    : 900
    """

