from random import choice

def rand(chess_board,team="black"):
  '''
    Choses a random move from a random black piece.
  '''

  team_pieces = []
  for tile in chess_board.pieces:
    if chess_board.pieces[tile]["team"] == team:
      team_pieces.append(tile)


  moves = []
  while len(moves) == 0:
    if chess_board.isKingInCheck(team) or len(team_pieces) == 0:
      return None

    tile = choice(team_pieces)
    team_pieces.remove(tile)

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

